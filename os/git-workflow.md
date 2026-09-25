---
id: os-git-workflow
title: "Git-Versionierung und Übergabe"
status: DRAFT
authority: proposed_operating_procedure
reviewed_on: "2026-09-25"
source_ids: ["S01"]
sensitivity: company_confidential
---

# Git-Versionierung und Übergabe

## Was du bekommst

Ein lokales Repository mit zwei nachvollziehbaren Zuständen: `v0.1-import` bewahrt die ursprünglichen 18 Markdown-Dateien; `v0.2` enthält den Neuaufbau. Der Import ist eine heutige Archivierung, keine rekonstruierte frühere Git-Historie. Das zusätzliche Bundle enthält die übertragbaren Git-Objekte und Referenzen.

## Alltag

Agent liest relevante Dateien → erstellt einen kleinen Änderungsentwurf → Kernänderungen werden freigegeben → Commit mit verständlicher Begründung → bei verbundenem Remote Upload in das private Repository. Git erledigt nicht selbst die inhaltliche Qualitätssicherung.

Eine Änderung an Strategie darf z. B. heißen: `Entscheidung: Pilot auf Refill-Marken begrenzen`. Eine reine Hypothese darf nicht so betitelt sein. Möglichst Quelle/Entscheidungs-ID im Commit nennen. Für Risikoänderungen separater Branch; für den Standardbetrieb keine unnötig komplizierte Branch-Struktur.

## Lesen und vergleichen

```bash
git log --oneline --decorate
git diff v0.1-import..v0.2 --stat
git show v0.2:company/current-state.md
```

Das Bundle lässt sich in ein neues lokales Repository klonen:

```bash
git clone company-brain-history.bundle company-brain
```

Erst nach bestätigter Verbindung einen **privaten** Remote unter dem richtigen Eigentümer anlegen. Nicht automatisch ein vorhandenes Repo überschreiben. Standardname als Vorschlag: `company-brain`, unabhängig vom späteren Brandnamen.

## Rechte und Sicherung

Das gesamte Repository und seine Historie sind zunächst nur für Jakob. Ein Dokument später zu löschen löscht es nicht aus älteren Commits. Bei Freigabe an Pascal/Kunden lieber eine freigegebene Teilmenge in einem eigenen Repository bereitstellen. Bei versehentlichem Geheimnis-Commit Zugang sofort sperren/rotieren und Historienbereinigung fachgerecht behandeln; `git revert` allein entfernt das Geheimnis nicht.

Lokales Repo und Bundle sind nicht automatisch Offsite-Backups. Das Paket zusätzlich an einem kontrollierten Speicherort sichern. Für Wiederherstellung regelmäßig das Bundle in einen frischen Ordner klonen und die Prüfungen ausführen.
