# PerformanceTestingTraining (Polish)

## WPROWADZENIE
##### SQL Server + MongoDB + Tableau Desktop + Python + Jmeter

##### Nie za krótkie wprowadzenie do testowania wydajności systemów opartych na bazach relacyjnych i nierelacyjnych. W tym odcinku porównamy wydajność baz SQLServer i MongoDB korzystając z klienta Tableau i API Flask (Python).

## INSTALACJA
### Narzędzia:
#### 1. SQL Server https://www.microsoft.com/en-us/sql-server/sql-server-editions-express
#### 2. MongoDB https://www.mongodb.com/download-center/community
#### 3. Robo 3T https://robomongo.org/
#### 4. Tableau Desktop https://www.tableau.com/products/desktop/download
#### 5. MongoDB BI Connector i ODBC driver https://www.mongodb.com/products/bi-connector i https://github.com/mongodb/mongo-odbc-driver/releases
#### 6. Jmeter https://jmeter.apache.org/download_jmeter.cgi
#### 7. Python https://www.python.org/download/releases/2.7/ lub w wersji jaką lubisz

### Konfiguracja i uruchomienie:
#### 1. Uruchomienie baz danych

##### 1.1 SQL Server - otwórz management studio i w nowym oknie (New Query) odpal zapytanie "Economy.sql". Zapytanie powinno utworzyć nową bazę "Economy"

##### 1.2 MongoDB - uruchom linię poleceń i poleceniem mongod odpal bazę na porcie 20717. Następnie uruchom klienta Robo3T. Utwórz nowe połączenie. W lewym menu na nowo otwartym połączeniu kliknij prawym przyciskiem myszy i stwórz nową bazę "Economy". Kliknij następnie prawym przyciskiem na bazę "Economy" i dodaj pierwszą kolekcję "YieldCurve"

#### 2. Podpięcie Tableau Desktop do SQL Server 

##### 2.1 Uruchom raport "Tableau_YieldCurve_SQLServer.twb". Zostaniesz poproszony o wprowadzenie informacji potrzebnych do połączenia z bazą danych SQL Server. Wzoruj się na załączonym poniżej zrzucie ekranu

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/TableauSQLServer.PNG)

#### 3. Podpięcie Tableau Desktop do MongoDB

##### 3.1 Uruchom raport "Tableau_YieldCurve_MongoDB.twb". Podobnie jak poniżej zostaniesz poproszony o wprowadzenie informacji potrzebnych do połączenia z bazą MongoDB. W tym celu musisz wpierw skonfigurować parę rzeczy:

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/TableauMongoDB.PNG)

##### 3.1.1 ODBC - uruchom ODBC Data Source Administrator. W zakładce [System DSN] dodaj nowy "MongoDB ODBC ANSI Driver". Kliknij przycisk [Finish]. Pojawi się okienko MongoDB ODBC Data Source Configuration. Wymyśl szybko nazwę użytkonika i hasło i wypełnij pola podobnie jak to jest pokazane na załączonym poniżej zrzucie ekranu.

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/ODBC.PNG)

##### 3.1.2 Dodanie nowego użytkownika do bazy MongoDB. Z zapamiętanym użytkownikiem i hasłem idziemy do MongoDB. W konsoli (CMD) odpalamy komendę "mongo localhost:27017/Economy". Następnie dodajemy nowego użytkownika do bazy "Economy" według wzoru przedstawionego na zrzucie ekranu poniżej. 

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/MongoConsole_AddUser.PNG)

##### Po pozytywnym dodaniu użytkownika przechodzimy do Robo3T i sprawdzamy czy istnieje nowo dodany użytownik. Ewentualnie poprawiamy wpisy jeśli się nie zgadzają z tym co jest przedstawione na zrzucie ekranu

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/robo3T_user.PNG)

##### 3.1.3 mongosqld - ostatnim krokiem jest uruchomienie Mongo BI connectora. W tym celu uruchomimy w konsoli komendę mongosqld z parametrami wzorowanymi na tych przedstawionych na zrzucie ekranu poniżej. Jeśli wszystko poszło ok, wróćmy na chwilę do konfiguratora MongoDB ODBC Data Source i przetestujmy połączenie. Jeśli jest ok to przejdźmy do Tableau i połączmy się z DataSourcem 

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/mongosqld.PNG)

#### 4. Uruchomienie API

##### 4.1. Otwórz konsolę cmd i wykonaj następujące czynności:

##### 4.1.1	"pip install flask"

##### 4.1.2 "pip install flask-restful"

##### 4.2 Będąc w katalogu "rest" wykonaj komendę "python api.py". Pojawią się błędy wynikające z niezainstalowanych bibliotek, które są wykorzystywane przez API. Doinstaluj je używając komendy "pip", w ten sam sposób co powyżej. Instalujemy brakujące biblioteki do skutku.


## ZAŁADOWANIE DANYCH

#### 1. MongoDB

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/MongoConsole_ImportData.PNG)

#### 2. SQL Server

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/SQLServer_Wizard.PNG)


## TESTY

##### Intro - Zapoznanie się z bazami i jakie zapytania będziemy wykonywali


#### Test Case 1 - Chcemy sprawdzić jak zmieniają się czasy wykonania zapytań na obu bazach przy użyciu Tableau Desktop wraz z ładowaniem danych testowych.

| Data Volume        | MongoDB           | SQL Server  |
| ------------- |:-------------:| -----:|
|                    | Rendering - Exec Query - DataSource - Layout | Rendering - Exec Query - Data Source - Layout |
|  250k              | |  |
|  500k              | |  |
|  750k              | |  |
|  1000k             | |  |


#### Test Case 2 - Chcemy sprawdzić czasy wykonania zapytań na obu bazach przy użyciu Tableau Desktop po połączniu głównej tabeli z kolejną tabelą.

| Query             | MongoDB           | SQL Server  |
| ------------- |:-------------:| -----:|
|                 | Rendering - Exec Query - Data Source - Layout | Rendering - Exec Query - Data Source - Layout |
|  JOIN           | |  |
|  CUSTOM QUERY   | |  |


#### Test Case 3 - Chcemy sprawdzić czasy wykonania złożonego zapytania na dużych danych w SSMS i CMD

| Query    | MongoDB           | SQL Server  |
| ------------- |:-------------:| -----:|
|  COUNT   |  | |
|  COUNT + JOIN   |  | |


#### Test Case 4 - Chcemy sprawdzić czasy wykonania zapytań na obu bazach przy użyciu Flask API dla małego i dużego ruchu. Do wygenerowania ruchu użyjemy narzędzia Jmeter. 

##### Mały ruch - 1 użytkownik (wątek) i 1 request
##### Duży ruch - 2 użytkowników (wątków), 2 requesty co 5 sekund w pętli (1,10)

| API Method + Query + Traffic        | MongoDB           | SQL Server  |
| ------------- |:-------------:| -----:|
|  GET + SELECT/FIND + Mały ruch            | |  |
|  GET + SELECT/FIND + Duży ruch            | |  |
|  GET + LEFT JOIN/LOOKUP + Mały ruch       | |  |
|  GET + LEFT JOIN/LOOKUP + Duży ruch       | |  |
