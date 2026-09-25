---
id: governance-data-ownership
title: "Wem gehört was — und wer darf es sehen?"
status: CORE
authority: user_architecture_with_required_rights_checks
reviewed_on: "2026-09-25"
source_ids: ["S01", "S05", "S07", "S10"]
sensitivity: founder_confidential
---

# Wem gehört was — und wer darf es sehen?

## Drei getrennte Bereiche

| Bereich | Gewünschte Zuordnung | Grenze |
|---|---|---|
| Company IP | Kreative Methoden, eigene Skills, Orchestrierung, Evaluationslogik, generische Vorlagen | Eigentum/Nutzungsrechte an fremden Beiträgen vertraglich sichern, nicht unterstellen |
| Client Brain | Kundenspezifische Marken-, Produkt-, Zielgruppen-, Asset- und Kampagnendaten | Möglichst beim Kunden; keine automatische Mitnahme oder Wiederverwendung bei anderen Kunden |
| Founder-private | Partnerverhandlung, vertrauliche wirtschaftliche Planung, persönliche Administration | Keine automatische Freigabe an Pascal, Kunden oder einen späteren Käufer |

## Entscheidender Architekturkonflikt

Wir wollen ein verkaufbares Unternehmen **und** kundeneigene Infrastruktur. Deshalb entsteht der Wert nicht daraus, einfach alle Kundendaten zu besitzen. Ein Käufer kann nur jene eigenen Rechte, Verfahren und Vertragsbeziehungen übernehmen, die tatsächlich übertragbar sind. Ein kundeneigenes Brand Brain kann zum Service dazugehören, ohne unser frei verkäufliches Eigentum zu sein.

## Was nicht ins Repo gehört

API-Keys, Tokens, Passwörter, Bankzugänge, vollständige private Chats, sensible persönliche Angaben, unerlaubt kopierte Kundendaten, nicht lizenzierte Fontdateien. Große Medien bleiben in dafür vorgesehenem Storage. Ein Asset-Link erteilt keine Nutzungsrechte.

## Freigaben

Die Beschriftung `company_confidential` oder ein Ordner `private/` ersetzt keine Zugriffskontrolle. Ein privates GitHub-Repo schützt gegenüber der Öffentlichkeit, nicht vor anderen eingeladenen Repo-Mitgliedern. Für unterschiedliche Personengruppen geeignete getrennte Ablagen nutzen.

## Zusammenarbeit und Übergabe

Mit Pascal klären: vorhandenes Wissen, neu erarbeitete Dokumentation, Nutzungsrechte, Bezahlung, Vertraulichkeit und Ausscheiden. Keine Behauptung „IP gehört automatisch der Firma“, solange das nicht vereinbart ist. Bei Genossenschaft → eigene Gesellschaft müssen Vertragspartner, Datenrechte, Accounts und Abrechnung jeweils geprüft werden; Rechnungsadresse ändern ist keine vollständige Rechtsübertragung.
