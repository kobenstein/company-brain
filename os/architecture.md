---
id: os-architecture
title: "Company OS — die kleinste tragfähige Architektur"
status: DECISION
authority: user_direction_with_verified_deployment_limits
reviewed_on: "2026-09-25"
source_ids: ["S01", "S07", "W05", "W07"]
sensitivity: company_confidential
---

# Company OS — die kleinste tragfähige Architektur

## Das System in einem Satz

**Ein Chat-Interface zum Arbeiten; ein versioniertes Gedächtnis zum Behalten; Fachsysteme für Dateien, Geld und echte Betriebsdaten.**

| Ebene | Aktuelle Richtung | Tatsächlicher Stand |
|---|---|---|
| CEO-Interface | ChatGPT; Business für gemeinsame betriebliche Nutzung prüfen | Bestehender privater Chat; neuer Business-Workspace nicht bestätigt |
| Firmenwissen | Markdown + privates Git-Repository | Lokal erstellt, Git-Versionierung vorhanden; Remote nicht bestätigt |
| Medien, Rechnungen, Verträge | Google Drive/Workspace | Architekturwahl diskutiert; Einrichtung hier nicht durchgeführt |
| Mail, Kalender, Calls | Gmail, Calendar, Meet | Geeignete Konten/Berechtigungen und Aufzeichnungstarif noch prüfen |
| Kundendaten | Möglichst im Kundenkonto; eindeutig getrennte Client Brains | Produkt-/Berechtigungsmodell offen, noch keine Kundeninstanzen |
| Finanzdaten | Buchhaltungssoftware + Bank als verbindliche Systeme | Rechtsform, Konto, Buchhaltung nicht festgelegt |
| Automationen | Erst einfache belegte Wiederholungen automatisieren | Keine produktive Automatisierung durch dieses Brain eingerichtet |

## Wozu Git, wozu Drive?

Git hält kleine Textdateien mit nachvollziehbaren Änderungen. Drive hält große Originaldateien und menschliche Arbeitsdokumente. Das Brain referenziert Medien mit dauerhaften IDs/Links, Rechten und Versionen; keine MP4-Bibliothek im Wissensrepo. Obsidian ist ein optionaler Viewer, kein Pflichttool und nicht die eigentliche Datenbasis.

## Modelle sind austauschbar

Google Workspace zwingt uns nicht zu Gemini. ChatGPT als Interface bedeutet umgekehrt nicht, dass künftig jede Aufgabe bei OpenAI laufen muss. Einen zweiten Modellanbieter erst hinzufügen, wenn ein konkreter Test einen relevanten Vorteil zeigt. Keine Mehrmodell-Orchestrierung auf Vorrat.

## Was wir ausdrücklich nicht voraussetzen

Ein Connector liefert nicht automatisch Schreibrechte, einen Trigger oder eine sichere Vollautomatisierung. Das Lesen einer GitHub-Datei ist etwas anderes als Commits schreiben. Ein Workspace-Agent ist nicht bereits ein funktionierender Company-Knowledge-Agent. Erst ein realer End-to-End-Test macht eine Verbindung produktiv.

## Neue Bausteine nur nach Bedarf

n8n für fehlende deterministische Verbindungen/Fehlerbehandlung; Datenbank für viele strukturierte Ereignisse; Vektor-Suche bei realen Suchproblemen; Portal bei wiederkehrender Freigabefriktion. Jev bleibt ungeprüfte Option. Keine dieser Komponenten ist für dieses lesbare Brain erforderlich.

[Status aller Einrichtungen](deployment-status.md) · [Geprüfte Plattformfähigkeiten](capability-register.md)
