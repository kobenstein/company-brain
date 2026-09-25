# On-demand company knowledge retrieval

## DECISION
Company knowledge must be available on demand while chatting, independently of the once-daily ingestion job. Retrieve the relevant context quickly and economically.

Source: Jakob, task `01a0d9d8-d503-7db0-8aa7-440abc572196` (Company Brain aktuell halten), 2026-09-25.
Confidence: explicit requirement; cross-chat automatic activation is not yet deployed or verified.

## Proposed retrieval procedure
1. Detect company-dependent requests: company plans, tools, prior decisions, customers, people, offers, methods or operating status.
2. Establish the latest accessible main revision. Use `INDEX.md` as a small topic router; read `company/current-state.md` for overall company direction. Reuse already-loaded material only while its revision remains valid.
3. Fetch the few relevant canonical files. Search by topic and aliases when useful; expand only if evidence is incomplete. Search results identify sources, so read the supporting entries before answering.
4. Empty search results do not prove knowledge is absent. Use the index/tree and direct file reads as a fallback. Report inability to verify rather than inventing history or asking Jakob to repeat retrievable decisions.
5. Prefer explicit decisions and corrections over assistant proposals. Distinguish current decisions, hypotheses and unresolved questions. Use original sources to resolve ambiguity and preserve customer access boundaries.
6. Answer using the retrieved context. Link supporting entries when useful. When freshness matters, disclose the latest successful source coverage; a daily snapshot is not live tool state. For a request about today's unsynced events, query the authorized live source if available or explain the gap.
7. Apply an explicit correction in the current conversation immediately. Durable saving follows the sync policy or an explicit immediate-save request; confirm a successful remote save before claiming it is in the Brain.

## Host setup still needed
Install a short startup/project instruction that names this repository and routes company questions here. Instructions stored only inside the repository do not load themselves in every ChatGPT chat. A skill can carry the procedure, but tools, permissions and host-side activation must be configured and tested separately. Do not assume every personal chat is readable by a cloud job.

## Initial routing
- Current direction and approved decisions: `company/current-state.md`, `company/decisions.md`.
- Planned tools and actual setup: `os/architecture.md`, `os/deployment-status.md`.
- Knowledge updates: `os/session-sync.md`, `os/knowledge-ingestion.md`.
- Pascal: `people/pascal.md`; do not infer an agreed role.
- Customer process: `product/client-journey.md`; confidential customer details require the separate authorized customer brain.
- Other topics: `INDEX.md`.

## Acceptance checks before claiming reliable operation
- Save a decision, then recover it in a fresh configured chat without a reminder.
- Retrieve the latest correction and identify superseded statements.
- Recover the documented tool plan even if the search service returns no results.
- Report source failures and stale coverage accurately.
- Keep confidential customer information within its assigned access scope.
- Verify a daily cloud run with the Mac off, including catch-up and deduplication.

## Observation on 2026-09-25
Direct file reads through the GitHub connection succeeded. A scoped search for `architecture` returned no results despite the existing file. This observation does not establish the cause or prove search is permanently unavailable; direct routing remains the fallback.
