# Báo Cáo Thu Hoạch Lab 17 - Multi-Memory Agent với Zep

**Học viên:** Phan Hoàng Dũng  
**Mã học viên:** 2A202601348  
**Repository:** `DungPhanHoangg05/DAY17_2A202601348_PhanHoangDung`

---

## 1. Trả lời 3 câu hỏi bắt buộc

1. **Layer quan trọng nhất trong bộ test này:**  
   **Long-term Memory (Declarative)** là layer quan trọng nhất (chiếm 4/11 ca đánh giá: E02, E03, E08, E09 và tham gia vào E07). Nó quyết định việc ghi nhớ preference xuyên session (E02), open-loop/deadline (E03), xử lý conflict & recency (E08 - `BLUEBIRD-42` dùng TypeScript/NestJS thay vì Python), và cô lập dữ liệu tuyệt đối giữa các user (E09 - Lan không bị lộ preference của Minh).

2. **Trade-off giữa Context Block (Zep) và Redis + Qdrant tự xây:**  
   - **Zep Context Block:** Managed service tự động trích xuất thực thể, đồ thị quan hệ, tổng hợp user context theo độ liên quan của thread, hỗ trợ temporal validity/recency mà không cần tự xây pipeline phức tạp.
   - **Redis + Qdrant:** Toàn quyền kiểm soát hạ tầng, latency thấp (0ms local), bảo mật on-premise nhưng tốn chi phí phát triển lớn để tự làm extraction, schema, indexing, ranking và context synthesis.

3. **Guardrail chống Memory Poisoning:**  
   Áp dụng mô hình **Dual-Gate & Provenance**: Phân tách rõ ràng giữa ephemeral working memory và durable memory. Chỉ ingest dữ liệu đã được sanitize PII và có `memory_opt_in`. Heartbeat chạy nền chỉ de-duplicate notes, đánh dấu stale task, tuyệt đối không tự nâng quyền hay nạp prompt injection vào durable state nếu không có user xác nhận.

---

## 2. Phân tích kết quả Benchmark

Dựa trên `reports/benchmark.md`, `reports/benchmark_no_memory.md` và `reports/comparison.md`:
- **Evidence Hit Rate:** `student` đạt **100.0% (11/11 PASS)** vs `no_memory` chỉ đạt **18.2% (2/11 PASS)** (Delta: +81.8%).
- **Average Retrieval Latency:** `student` là **11613.1 ms** vs `no_memory` là **0.0 ms**.
- **Average Token Reduction:** `student` đạt **14.6%** vs `no_memory` đạt **81.8%**.

1. **Layer có hit rate thấp nhất:**  
   Ở bản `student`, toàn bộ các layer đều đạt hit rate 100% (11/11). Tuy nhiên, trên baseline `no_memory`, các layer **Long-term (E02, E03, E08, E09)**, **Episodic (E04, E05)** và **Semantic (E06, E11)** đều có hit rate **0% (0/8 PASS)**; chỉ riêng **Short-term Memory (E01, E10)** đạt **100% (2/2 PASS)** nhờ xử lý in-thread.
2. **Query retrieve nhiều token nhất:**  
   **E02 (867 tokens)**, **E03 (866 tokens)** và **E08 (860 tokens)** là các query retrieve nhiều token nhất từ Long-term Context Block.
3. **Case mixed (E07):**  
   E07 (485 tokens, latency 72014.3 ms) kết hợp **Long-term Memory** (lấy preference cá nhân `Python` của Minh) và **Semantic Memory** (lấy domain guideline `Idempotency-Key`).
4. **Token reduction so với full source context:**  
   Bản `student` đạt trung bình **14.6%** token reduction (với E06 giảm 72.3%, E11 giảm 74.2%, E07 giảm 14.2%). Baseline `no_memory` có reduction cao hơn (**81.8%**) do 9/11 case không retrieve gì (100% reduction, 0 token), dẫn đến hit rate tụt thảm hại xuống 18.2%. Điều này chứng minh token reduction chỉ có ý nghĩa khi đi kèm evidence hit rate cao.

---

## 3. Nhận xét về Recency (E08) và Compaction (E10)

- **Recency (E08):** Case E08 PASS thành công với đầy đủ markers `BLUEBIRD-42`, `TypeScript`, `NestJS` nhờ Zep cập nhật preference theo scope dự án mới mà vẫn duy trì provenance cho dự án `ORCHID-27`.
- **Compaction (E10):** Case E10 PASS (195 tokens) trên fixture 14 turns nhờ cơ chế sliding window kết hợp `<DURABLE_NOTES>` giữ lại chính xác constraint `REVIEW-DEADLINE-1600`, `Friday`, `16:00` dù raw turn ban đầu đã bị evict khỏi recent buffer.
