# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **11613.1 ms**
- Average token reduction vs full source context: **14.6%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 17218.6 | 127 | 72.3% |  |
| E09 | long_term | PASS | 28521.1 | 652 | 0.0% |  |
| E10 | short_term | PASS | 0.3 | 195 | 0.0% |  |
| E02 | long_term | PASS | 2167.6 | 867 | 0.0% |  |
| E03 | long_term | PASS | 2638.6 | 866 | 0.0% |  |
| E04 | episodic | PASS | 311.8 | 284 | 0.0% |  |
| E05 | episodic | PASS | 2424.7 | 303 | 0.0% |  |
| E07 | mixed | PASS | 72014.3 | 485 | 14.2% |  |
| E11 | semantic | PASS | 596.0 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1850.7 | 860 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`ENTITY: Payment API Retry Policy - For POST /payments, every retryable request must send the same Idempotency-Key. Retries are permitted only for HTTP 429 or transient 5xx errors, employing exponential-backoff, and ceasing after a maximum of three retries. This is marked as PAYMENT-RULE-3 from internal-api-guideline-v3. ENTITY: POST /payments -  ENTITY: max-3-retries -  ENTITY: PAYMENT-RULE-3 -  ENTITY: exponential-backoff -  ENTITY: Idempotency-Key -  ENTITY: transient 5xx errors -  ENTITY: HTTP 429 - `

### E09 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python in that context. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. `

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is currently debugging async HTTP requests for an incident identified as ASYNC-FIX-20. A task is to complete a benchmark report, identified as open loop LAB-REPORT-1600, before Friday at 4:00 PM. The debugging efforts involved attempting to increase the timeout to 60 seconds, checking the connection pool, client lifecycle, and concurrency. The effective solution involved reusing an aiohttp ClientSession and setting concurrency to 20, addressing connection churn rather than the timeou`

### E03 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is currently debugging async HTTP requests for an incident identified as ASYNC-FIX-20. A task is to complete a benchmark report, identified as open loop LAB-REPORT-1600, before Friday at 4:00 PM. The debugging efforts involved attempting to increase the timeout to 60 seconds, checking the connection pool, client lifecycle, and concurrency. The effective solution involved reusing an aiohttp ClientSession and setting concurrency to 20, addressing connection churn rather than the timeou`

### E04 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + con`

### E05 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: `

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is currently debugging async HTTP requests for an incident identified as ASYNC-FIX-20. A task is to complete a benchmark report, identified as open loop LAB-REPORT-1600, before Friday at 4:00 PM. The debugging efforts involved attempting to increase the timeout to 60 seconds, checking the connection pool, client lifecycle, and concurrency. The effective solution involved reusing an aiohttp ClientSession and setting concurrency to 20, addressing connection churn rather tha`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<USER_SUMMARY> Minh's personal project is named ORCHID-27 and prefers Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. Minh is currently debugging async HTTP requests for an incident identified as ASYNC-FIX-20. A task is to complete a benchmark report, identified as open loop LAB-REPORT-1600, before Friday at 4:00 PM. The debugging efforts involved attempting to increase the timeout to 60 seconds, checking the connection pool, client lifecycle, and concurrency. The effective solution involved reusing an aiohttp ClientSession and setting concurrency to 20, addressing connection churn rather than the timeou`
