# Bundestag Lobbyregister API

API des Deutschen Bundestags zum [Lobbyregister](https://www.lobbyregister.bundestag.de/startseite) für die Interessenvertretung gegenüber dem Deutschen Bundestag und der Bundesregierung.

Am 1. Januar 2022 trat das Lobbyregistergesetz in Kraft. Es verlangt, dass alle Personen und Organisationen, die mit Mitgliedern des Bundestages oder der Bundesregierung Kontakt aufnehmen, um politischen Einfluss zu nehmen, sich registrieren lassen. Die Nichtbeachtung dieser Pflicht oder die ungenaue, unvollständige oder verspätete Registrierung kann mit einer Geldstrafe von bis zu 50.000 Euro geahndet werden. Weitere Informationen sind online verfügbar unter https://www.lobbyregister.bundestag.de/informationen-und-hilfe.


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
