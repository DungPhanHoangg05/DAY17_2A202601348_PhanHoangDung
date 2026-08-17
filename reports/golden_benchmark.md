# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1120.3 ms**
- Average token reduction vs full source context: **14.5%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.3 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 2071.9 | 611 | 0.0% |  |
| G09 | semantic | PASS | 311.0 | 148 | 67.8% |  |
| G10 | semantic | PASS | 386.3 | 95 | 79.3% |  |
| G14 | mixed | PASS | 1598.9 | 431 | 0.0% |  |
| G03 | long_term | PASS | 1301.6 | 864 | 0.0% |  |
| G04 | long_term | PASS | 1586.4 | 859 | 0.0% |  |
| G07 | episodic | PASS | 299.3 | 629 | 0.0% |  |
| G08 | episodic | PASS | 290.5 | 604 | 0.0% |  |
| G11 | mixed | PASS | 1433.6 | 439 | 22.3% |  |
| G13 | mixed | PASS | 596.2 | 406 | 28.1% |  |
| G15 | mixed | PASS | 1935.4 | 736 | 0.0% |  |
| G16 | mixed | PASS | 1642.3 | 484 | 14.3% |  |
| G17 | mixed | PASS | 1627.9 | 484 | 14.3% |  |
| G18 | mixed | PASS | 609.1 | 403 | 28.7% |  |
| G19 | mixed | PASS | 1837.6 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1613.6 | 868 | 0.0% |  |
| G12 | mixed | PASS | 1939.3 | 431 | 31.8% |  |
| G20 | mixed | PASS | 1325.2 | 609 | 3.6% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </EPISODES>  <FA`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.`

### G10 - semantic

`EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </EP`

### G03 - long_term

`<USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For personal project`

### G04 - long_term

`<USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For personal project`

### G07 - episodic

`EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cong ty yeu cau chinh context window cho agent tren dung backend du an cong ty. Minh can biet stack bat buoc cua BLUEBIRD va ty le budget bon tang nho trong lab de cau hinh cho dun EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi:`

### G08 - episodic

`EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHI EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Trong thread nay minh vua nhac constraint gio sta`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For pers`

### G13 - mixed

`<EPISODIC> EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cong ty yeu cau chinh context window cho agent tren dung backend du an cong ty. Minh can biet stack bat buoc cua BLUEBIRD va ty le budget bon tang nho trong lab de cau hinh cho dun EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Pyt`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For pers`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For pers`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For pers`

### G18 - mixed

`<EPISODIC> EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cong ty yeu cau chinh context window cho agent tren dung backend du an cong ty. Minh can biet stack bat buoc cua BLUEBIRD va ty le budget bon tang nho trong lab de cau hinh cho dun EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preferen`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For pers`

### G05 - long_term

`<USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For personal project`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on two projects: BLUEBIRD-42, which requires a TypeScript/NestJS backend, and ORCHID-27, a personal project that uses Python. Minh also needs to complete a benchmark report for an open loop LAB-REPORT-1600 before Friday at 16:00. Previously, Minh was debugging async HTTP issues related to connection churn and the ASYNC-FIX-20 incident, which were resolved by reusing the aiohttp ClientSession and setting concurrency to 20.  Minh prefers Python and dislikes Java. When explaining code, Minh prefers short examples. Minh is interested in learning about async/await and prefers explanations using a timeline for topics like coroutines versus Tasks. For pers`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
