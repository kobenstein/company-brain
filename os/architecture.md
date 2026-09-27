# Company OS Architecture

## Principle
Keep the system simple until real work proves the need for more layers.

## ChatGPT Business
Intended primary CEO / agent interface.

## Company Brain
English Markdown + private Git repository as durable, version-controlled company memory.

## Google Workspace / Drive
Future operational layer for email, calendar, Meet, large media, PDFs, contracts and working files once company/domain identity is ready.

## Specialist systems
Accounting, ad platforms, CRM and other tools remain source-of-truth for their domain.

## Models
Model-agnostic. OpenAI can be primary; other models may be used where a concrete task advantage exists.

## Automation
Do not add n8n, Jev or custom infrastructure until native workflows fail or repeated complexity justifies them.

## Cost measurement / observability
Cost attribution must be considered from the start when designing agentic client workflows, even if the first implementation stays lightweight.

The system should make it possible to attribute AI and tool usage at least by:
- client / customer
- agent or workflow
- provider / tool
- model or generation type where practical
- date / run

Relevant external costs (for example OpenAI / Workspace-agent usage, fal.ai, Runway, Higgsfield or other generation providers) should be combinable into a per-client cost view.

Do not rely on a provider's shared workspace billing alone as the long-term customer cost-accounting layer. Prefer an internal usage/cost log once workflow volume justifies it, so margins and customer economics can be measured reliably.
