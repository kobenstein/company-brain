---
id: finance-account-registry
title: "Konten, Kosten und Zuständigkeiten"
status: DRAFT
authority: proposed_account_control
reviewed_on: "2026-09-25"
source_ids: ["S01", "S07"]
sensitivity: founder_confidential
---

# Konten, Kosten und Zuständigkeiten

## Kleine Accountliste statt Tool-Wildwuchs

Für jedes tatsächlich verwendete System erfassen: Name, Zweck, rechtlicher Vertragspartner, Billing-Empfänger, verantwortlicher Admin, Daten-/IP-Inhaber, Tarif/Datum, Zahlungsweg, erlaubte Nutzer, Kündigung/Export und Übertragbarkeit. **Keine Passwörter oder API-Schlüssel in diese Liste.**

| System | Bisherige Rolle im Plan | Entscheidung/Einrichtung |
|---|---|---|
| ChatGPT Business | Gemeinsames KI-Interface, mögliche Workspace Agents | Gewünscht, noch nicht eingerichtet |
| GitHub | Privates versioniertes Brain | Lokal Git vorhanden; Remote-Verbindung offen |
| Google Workspace | Mail, Meet, Calendar, Drive | Richtung bevorzugt; Domain, Plan, Rechtsträger offen |
| Qonto | Konto/Karte/Belegautomatisierung | Diskutierter Favorit, kein Konto eröffnet; AT-Zulassung, Tarif und Integration erneut prüfen |
| Revolut Business | Alternative für internationale Zahlungen/API | Diskutiert, keine Auswahl bestätigt |
| Buchhaltung | Verbindliche Finanzdaten, Steuerberaterübergabe | Tool/Schnittstelle offen |
| Creative APIs | Bild, Video, Audio, Analyse | Je Use Case wählen und Verbrauch messen |

## Kostenprinzipien

Modelle, Video-Credits, Fehlgenerationen, Speicher, menschlicher Review und Wartung gemeinsam messen. n8n ist nicht automatisch günstiger oder teurer als ein Workspace-Agent. Unterschiedliche Kontingente, Zusatzcredits und API-Abrechnung erst an einem realen Ablauf vergleichen. Alte konkrete Tarifzahlen werden nicht als aktuelle Fakten übernommen.

## Automatisierungsgrenzen

Belege erfassen und zuordnen ist etwas anderes als steuerlich korrekt verbuchen oder eine Zahlung freigeben. Fachsoftware hält Transaktionen; KI erklärt Auffälligkeiten und bereitet Entscheidungen vor. Keine Zahlungsautonomie ohne ausdrückliche Grenzen und Berechtigungen.

## Account-Migration

Billing, Vertragspartner, Admin-Rechte, Datenrechte und technischer Zugriff getrennt behandeln. Beim späteren Exit wird kein persönliches Passwort „mitverkauft“. Dokumentation soll eine kontrollierte Übergabe ermöglichen, nicht automatisch Rechte schaffen.
