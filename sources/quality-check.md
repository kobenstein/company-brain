---
id: sources-quality-check
title: "Qualitätsprüfung und verbleibende Grenzen"
status: CURRENT
authority: executed_structural_checks_with_limits
reviewed_on: "2026-09-25"
source_ids: ["S01", "S03", "S11"]
sensitivity: company_confidential
---

# Qualitätsprüfung und verbleibende Grenzen

## Tatsächlich ausgeführte technische Prüfungen

Stand: 25.09.2026, v0.2.

| Prüfung | Ergebnis |
|---|---|
| Markdown-Dateien mit Metadaten | **75** |
| Pflichtfelder, eindeutige IDs und dokumentierte Statuswerte | Bestanden |
| Quellen-IDs gegen Quellenregister | Bestanden |
| Lokale Markdown-Links | **158** geprüft; keine fehlenden Ziele |
| Marktstudie | **6 Blätter, 1306 nichtleere Zellen** gegen ihre Markdown-Fassung geprüft; keine ausgelassenen Zellinhalte |
| Konkrete Marktforschungsdatensätze | 73 Firmen, 23 Belege, 17 Orte, 10 Sprachthemen, 12 Qualifikationsfelder erhalten |
| Einfacher Secret-Mustercheck | Keine Treffer für die implementierten API-/Schlüssel-Muster; kein vollständiges Security-Audit |
| Private Kontexte in den übernommenen Altdateien | Zwei dokumentierte minimale Redaktionen; keine vollständigen privaten Chat-Exporte übernommen |
| Navigierbarkeit | Kurzer Einstieg + Detailindex + separate historische Archive |

## Git- und Paketprüfung

Der Abschlusslauf prüft Git-Objekte und Bundle, klont die Git-Historie in einen frischen Ordner, führt dort dieselbe Strukturprüfung aus und vergleicht jedes gepackte Dateibyte mit seinem SHA-256-Eintrag. Das technische Ergebnis wird zusätzlich als `VALIDATION.json` im äußeren Downloadpaket abgelegt; nicht aus einer bloßen Absicht als erfolgreichen Cloud-Upload lesen.

## Was nicht als bestanden behauptet wird

Kein vollständiger Volltextscan aller Account-Chats; keine unabhängige Verifikation aller historischen Onlinequellen; keine Rechtsprüfung; keine bewiesene Nachfrage oder Kampagnenwirkung; kein produktiver Agentenlauf; kein GitHub-Remote-Upload. Die 18 [Abnahmefragen](../tests/memory-acceptance.md) sind eine Testvorlage für die spätere Anbindung, noch kein gemessener Agenten-Benchmark.

## Erneut prüfen

```bash
python3 scripts/check_brain.py
```

Der Checker liest nur lokale Dateien. Er benötigt keine Zugangsdaten, Netzwerkverbindung oder neuen Konten.
