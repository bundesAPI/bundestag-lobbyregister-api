# Bundestag Lobbyregister API

API des Deutschen Bundestags zum [Lobbyregister](https://www.lobbyregister.bundestag.de/startseite) für die Interessenvertretung gegenüber dem Deutschen Bundestag und der Bundesregierung.

Am 1. Januar 2022 ist das Gesetz zur Einführung eines Lobbyregisters für die Interessenvertretung gegenüber dem Deutschen Bundestag und gegenüber der Bundesregierung vom 16. April 2021 (Lobbyregistergesetz – LobbyRG) in Kraft getreten.
Das Lobbyregistergesetz wurde am 16. April 2021 im Bundesgesetzblatt verkündet (BGBl. 2021 I S. 818, Anhang 1).
In das Lobbyregister müssen sich alle natürlichen Personen und Organisationen eintragen, die Kontakt zu Mitgliedern des Bundestages oder der Bundesregierung aufnehmen, um Einfluss auf politische Prozesse zu nehmen, oder die solche Tätigkeiten in Auftrag geben, wenn ihre Tätigkeit eine im Gesetz definierte Erheblichkeitsschwelle überschreitet und wenn keine der im Gesetz vorgesehenen Ausnahmen vorliegt. Auch eine freiwillige Eintragung ist möglich.
Wer sich trotz bestehender Registrierungspflicht nicht einträgt oder Eintragungen unrichtig, unvollständig oder nicht rechtzeitig vornimmt, begeht eine Ordnungswidrigkeit, die mit einer Geldbuße von bis zu 50.000 Euro geahndet werden kann.
Weitere Informationen zum Hintergrund finden sich online unter
https://www.lobbyregister.bundestag.de/informationen-und-hilfe


## Registereinträge Detailprofile

**URL:** https://www.lobbyregister.bundestag.de/sucheDetailJson
	
Die API zum Lobbyregister bietet Nutzer/-innen die Möglichkeit, die öffentlichen Daten zu Detailprofilen der registrierten Interessenvertreter/-innen im JSON Format herunterzuladen, potenziell gefiltert und sortiert u.a. auf Basis folgender GET-Parameter:


**Parameter:** *q* (Optional)

Query String: Enthält die angegebene Suchanfrage - einen Text, der in einem der Textfelder vorkommen muss. Wird der Parameter nicht gesetzt, werden alle Registereinträge ausgegeben.

Sie können mithilfe von Anführungszeichen Ihre Suchergebnisse auf exakte Treffer beschränken, z. B. "Energie" statt Energie. Mithilfe der booleschen Operatoren UND, ODER, NICHT und durch die Verwendung von Klammern () können Sie außerdem Ihre Suchanfrage verfeinern.


**Parameter:** *sort* (Optional)

- "REGISTRATION_ASC"
- "REGISTRATION_DESC"
- "NAME_ASC"
- "NAME_DESC"
- "NUMBEROFEMPLOYEES_ASC"
- "NUMBEROFEMPLOYEES_DESC"
- "FINANCIALEXPENSES_ASC"
- "FINANCIALEXPENSES_DESC"

Sortierungs-Kriterium: 
"REGISTRATION_ASC"=Sortierung nach Registernummer in aufsteigender Reihenfolge; 
"REGISTRATION_DESC"=Sortierung nach Registernummer in absteigender Reihenfolge; 
"NAME_ASC"=Sortierung nach Name in aufsteigender Reihenfolge; 
"NAME_DESC"=Sortierung nach Name in absteigender Reihenfolge; 
"NUMBEROFEMPLOYEES_ASC"=Sortierung nach Angestellten in aufsteigender Reihenfolge; 
"NUMBEROFEMPLOYEES_DESC"=Sortierung nach Angestellten in absteigender Reihenfolge; 
"FINANCIALEXPENSES_ASC"=Sortierung nach Höhe der finanziellen Aufwendungen in aufsteigender Reihenfolge (beginnend mit Einträgen ohne Angabe); 
"FINANCIALEXPENSES_DESC"=Sortierung nach Höhe der finanziellen Aufwendungen in absteigender Reihenfolge;
 
Wird der Parameter nicht gesetzt wird die erste Option als Kriterium herangezogen.


### Alternative Zugänge

Eine Vorschau der o.g. Ergebnisse lässt sich unter Verwendung der o.g. GET-Parameter von https://www.lobbyregister.bundestag.de/sucheJson beziehen. Auch lassen sich über diverse Filter-Parameter Teilmengen der Einträge beziehen (z.B. filter%5Bfieldsofinterest%5D%5BFOI_WORK%7CFOI_WORK_POLICY%5D=true).
Die Ergebnisse zu einzelnen Registereinträgen lassen sich wiederum über die Pfad-Parameter Registernummer *registerNumber* und Interessenvertreter/-innen-ID *registerEntryDetail-id* auch gezielt von https://www.lobbyregister.bundestag.de/suche/{registerNumber}/{registerEntryDetail-id} beziehen.


## Beispiel

```bash
interessenvertretungen=$(curl -m 60 'https://www.lobbyregister.bundestag.de/sucheDetailJson?sort=FINANCIALEXPENSES_DESC')
```
