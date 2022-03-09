# Bundestag Lobbyregister API

API des Deutschen Bundestags zum Lobbyregister für die Interessenvertretung gegenüber dem Deutschen Bundestag und der Bundesregierung.


## Registereinträge Detailprofile

**URL:** https://www.lobbyregister.bundestag.de/sucheDetailJson
	
Die API zum Lobbyregister bietet Nutzer/-innen die Möglichkeit, die öffentlichen Daten zu Detailprofilen der registrierten Interessenvertreter/-innen im JSON Format herunterzuladen, potenziell gefiltert und sortiert u.a. auf Basis folgender GET-Parameter:


**Parameter:** *q* (Optional)

Query String: Enthält die angegebene Suchanfrage - einen Text, der in einem der Textfelder vorkommen muss. Wird der Parameter nicht gesetzt, werden alle Registereinträge ausgegeben.


**Parameter:** *sort* (Optional)

- "REGISTRATION_ASC"
- "REGISTRATION_DESC"
- "NAME_ASC"
- "NAME_DESC"
- "FINANCIALEXPENSES_ASC"
- "FINANCIALEXPENSES_DESC"

Sortierungs-Kriterium: 
"REGISTRATION_ASC"=Sortierung nach Registernummer in aufsteigender Reihenfolge; 
"REGISTRATION_DESC"=Sortierung nach Registernummer in absteigender Reihenfolge; 
"NAME_ASC"=Sortierung nach Name in aufsteigender Reihenfolge; 
"NAME_DESC"=Sortierung nach Name in absteigender Reihenfolge; 
"FINANCIALEXPENSES_DESC"=Sortierung nach Höhe der finanziellen Aufwendungen in aufsteigender Reihenfolge (beginnend mit Einträgen ohne Angabe); 
"FINANCIALEXPENSES_DESC"=Sortierung nach Höhe der finanziellen Aufwendungen in absteigender Reihenfolge; 
Wird der Parameter nicht gesetzt wird die erste Option als Kriterium herangezogen.


### Alternative Zugänge

Eine Vorschau der o.g. Ergebnisse lässt sich unter Verwendung der o.g. GET-Parameter von https://www.lobbyregister.bundestag.de/sucheJson beziehen. 
Die Ergebnisse zu einzelnen Registereinträgen lassen sich wiederum über die Pfad-Parameter Registernummer *registerNumber* und Interessenvertreter/-innen-ID *registerEntryDetail-id* auch gezielt von https://www.lobbyregister.bundestag.de/suche/{registerNumber}/{registerEntryDetail-id} beziehen.


## Beispiel

```bash
interessenvertretungen=$(curl -m 60 'https://www.lobbyregister.bundestag.de/sucheDetailJson?q=Security&sort=FINANCIALEXPENSES_DESC')
```
