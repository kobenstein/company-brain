---
id: inbox-idea-drop
title: "Idea Drop — ein Eingang für Ideen und Links"
status: DECISION
authority: user_requirement_with_initial_entries
reviewed_on: "2026-09-25"
source_ids: ["S01", "S07", "S08", "S10"]
sensitivity: company_confidential
---

# Idea Drop — ein Eingang für Ideen und Links

## Das gewünschte Verhalten

Jakob wirft eine Idee oder einen Link hinein, möglichst ohne Formular. Das System ergänzt Eingangsdatum, Quelle, kurze Bedeutung, Thema, Status und nächsten sinnvollen Schritt. **Automatischer Import ist noch nicht installiert.** Dieses Dokument ist der erste portable Eingang.

| ID | Eingang | Inhalt | Status | Wohin / nächster Schritt |
|---|---|---|---|---|
| ID-001 | 21.09.2026, laut Gesprächskontext | [Founder-Institute-Guide](https://fi.co/insight/how-to-build-a-startup-with-ai-in-2026-the-ai-native-founder-s-guide) | Ressource gesichert; Webquelle im Neuaufbau erreichbar | Academy / AI-native Unternehmensaufbau |
| ID-002 | 21.09.2026, laut Gesprächskontext | [YouTube Z3JyAqh4ixg](https://www.youtube.com/watch?v=Z3JyAqh4ixg) | Link gesichert, vollständiger Inhalt nicht ausgewertet | Transcript prüfen; keine Zusammenfassung erfinden |
| ID-003 | 24.–25.09.2026, genaue Uhrzeit offen | Konkrete Kundenfrage → Video-Landingpage → Kauf/Anfrage | Hypothese | Nach Ads-Pilot gesondert testen |
| ID-004 | 24.–25.09.2026 | Customer Taste und Market Performance getrennt rückführen | Produktprinzip im Brain dokumentiert | Bei Client-Feedback-Schema berücksichtigen |

## Minimaler Datensatz

`id`, `captured_at`, `source_url_or_note`, `source_date_if_known`, `one_sentence_relevance`, `topic`, `status`, `next_action_or_none`.

Erfassungsdatum und Veröffentlichungsdatum sind verschieden. Ein erfolgreicher Link-Drop beweist nicht, dass die Webseite gelesen wurde. Doppelter Link wird ergänzt statt mehrfach als neue Erkenntnis gespeichert. Sensible Inhalte zuerst klassifizieren.

[Wissen erfassen](../os/knowledge-ingestion.md) · [Ressourcen](../academy/resources.md)
