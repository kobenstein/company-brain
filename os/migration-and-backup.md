---
id: os-migration-and-backup
title: "Migration — erst sichern, dann überführen"
status: DRAFT
authority: proposed_migration_with_current_limits
reviewed_on: "2026-09-25"
source_ids: ["S01", "S07", "W08"]
sensitivity: company_confidential
---

# Migration — erst sichern, dann überführen

## Empfohlener Weg für diesen gemischten privaten Verlauf

Das kuratierte Unternehmenswissen separat in den Firmenbereich übernehmen, persönliche Inhalte getrennt halten. Das ist eine redaktionelle Übernahme, **kein** vollständiger Workspace-Merge. Dieses Paket führt keine Kontomigration durch.

## Aktuell dokumentierte Grenzen

OpenAI beschreibt den persönlichen→Business-Merge als dauerhaft. Nicht alles wird übernommen, unter anderem gehen Custom Instructions nicht mit. Historische Chats können ausnahmsweise später nicht abrufbar sein; wichtige Inhalte vorher sichern. In Business ist der reguläre Datenexport nicht verfügbar. Mobile Abos müssen separat verwaltet werden; eine Apple-Rückerstattung ist kein garantiertes Ergebnis unserer Migration. [Offizielle Hilfe](https://help.openai.com/en/articles/8801890)

## Sichere Reihenfolge

1. Verfügbare ursprüngliche Dateien und wichtige geschäftliche Quellen sichern; für vollständige historische Abdeckung wäre zusätzlich ein eigener Account-Export die bessere Kontrollbasis.
2. Dieses Brain, seine Quellenabdeckung und offenen Konflikte festhalten. Sensible Privat-/Partnerinformationen nicht in gemeinsam freigegebene Bereiche kopieren.
3. Eigentümer, Vertragspartner, Zugriffe und gewünschten Tarif prüfen. Noch keinen unnötigen Merge oder neue Käufe durchführen.
4. Eine erlaubte Wissensfrage, eine neue Idee und eine bestätigte Entscheidung durch die Zieloberfläche testen.
5. Erst nach erfolgreichem Zugriff Schreibrechte, Automationen und weitere Personen schrittweise ergänzen.

## Backup-Regel

Versioniertes Repo plus unabhängige exportierte Sicherung. Große Medien und operative Systeme haben eigene Backups. Ein erfolgreiches Git-Paket enthält keine vollständige Sicherung von Google Drive, ChatGPT oder Kundenaccounts.
