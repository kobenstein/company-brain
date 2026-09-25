---
id: os-capability-register
title: "Plattformfähigkeiten — geprüft, offen oder nur geplant"
status: RESEARCH
authority: current_primary_docs_with_explicit_gaps
reviewed_on: "2026-09-25"
source_ids: ["S01", "W05", "W06", "W07"]
sensitivity: company_confidential
---

# Plattformfähigkeiten — geprüft, offen oder nur geplant

**Stand: 25.09.2026.** Dokumentation belegt eine beschriebene Fähigkeit, nicht deren Freischaltung in Jakobs konkretem Konto.

| Fähigkeit | Einordnung |
|---|---|
| Workspace Agents mit Modell/Reasoning-Einstellung, Tools/Skills, Zeitplan und API-Trigger | In offizieller OpenAI-Hilfe beschrieben (W05) |
| Menschliche Freigaben für Schreibaktionen | Dokumentiert; passend zum Risiko konfigurieren und testen (W05) |
| Automatische Modellwahl pro einzelnem Schritt | In den geprüften Stellen nicht ausreichend belegt; nicht aus Agent-Modellwahl ableiten |
| Native Gmail-Eingangsereignisse starten unseren gesamten Workflow | Frühere Aussage hier nicht verifiziert; Trigger separat demonstrieren |
| Agenten-Antworten per Trigger-API abrufen | Dokumentationskonflikt: Hilfe nennt 202 ohne Run-ID/Abruf, Developer-Doku beschreibt Run-Abruf. Nicht darauf implementieren, bevor konkret getestet (W05/W06) |
| GitHub-Wissen lesen | Offizielle Anbindung beschrieben; konkreter Repozugriff nötig (W07) |
| GitHub-Commits schreiben | Benötigt tatsächlich verfügbaren Schreibweg/Berechtigung; aktuell keine bestätigte Verbindung |
| Komplettes privates Chatarchiv automatisch ins Brain synchronisieren | Nicht eingerichtet; historische Suche ist kein Ereignisstream |
| Private ChatGPT-Fragen einer Zielgruppe mit exaktem Volumen abrufen | Nicht als verfügbare Datenquelle bestätigt |

[Agent-Hilfe](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business) · [Trigger-Dokumentation](https://developers.openai.com/workspace-agents/trigger-runs) · [GitHub-Hilfe](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)

## Konsequenz für den Aufbau

Ein kleines Testereignis und eine erlaubte Änderung vollständig nachweisen. Bei fehlendem Trigger kann später ein anderer Orchestrator nötig sein; n8n deshalb weder grundsätzlich streichen noch vorsorglich installieren. Kosten, Tokenlimits, konkrete Modellnamen und Abos nicht aus alten Chatantworten als aktuell übernehmen.
