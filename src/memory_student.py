from __future__ import annotations

import json
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        return user_context.context or ""

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        query = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=query,
                scope="episodes",
                limit=8,
            )
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=query,
                scope="nodes",
                limit=8,
            )
        return self._render_semantic_results(results)

    @staticmethod
    def _render_semantic_results(results: Any) -> str:
        """Keep semantic evidence compact without dropping literal markers.

        The lab seeds every knowledge item as both JSON and plain text. Zep can
        therefore return the same summary twice; rendering the full JSON plus
        metadata lets those duplicates consume the semantic layer's 3% budget.
        Normalize JSON episodes to their summary and deduplicate them before
        ContextBudgetManager trims the layer.
        """
        rendered: list[str] = []
        seen: set[str] = set()

        for episode in getattr(results, "episodes", None) or []:
            raw_content = getattr(episode, "content", None)
            if not raw_content:
                continue

            content = str(raw_content).strip()
            try:
                document = json.loads(content)
            except (TypeError, ValueError, json.JSONDecodeError):
                document = None

            if isinstance(document, dict) and document.get("summary"):
                content = str(document["summary"]).strip()

            dedupe_key = " ".join(content.casefold().split())
            if not dedupe_key or dedupe_key in seen:
                continue
            seen.add(dedupe_key)
            rendered.append(f"EPISODE: {content}")

        # The nodes-scope compatibility fallback has no episodes to compact.
        return "\n".join(rendered) if rendered else render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
