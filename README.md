# PerformanceTestingTraining (Polish)

## WPROWADZENIE
[![GitHub issues](https://img.shields.io/github/issues/przemastro/performance-testing-training-polish)](https://github.com/przemastro/performance-testing-training-polish/issues)
[![GitHub forks](https://img.shields.io/github/forks/przemastro/performance-testing-training-polish)](https://github.com/przemastro/performance-testing-training-polish/network)
[![GitHub stars](https://img.shields.io/github/stars/przemastro/performance-testing-training-polish)](https://github.com/przemastro/performance-testing-training-polish/stargazers)
[![SQL Server version](https://img.shields.io/badge/TSQL-2012-%23ccc)](https://github.com/przemastro/performance-testing-training-polish)
[![Python version](https://img.shields.io/badge/Python-2.7.x-%233572A5)](https://github.com/przemastro/performance-testing-training-polish)

##### Nie za krótkie wprowadzenie do testowania wydajności systemów opartych na bazach relacyjnych i nierelacyjnych. W tym odcinku porównamy wydajność baz SQLServer i MongoDB korzystając z klienta Tableau i API Flask (Python).

## INSTALACJA
### Repozytorium
#### 1. Sklonuj repozytorium: https://github.com/przemastro/performance-testing-training-polish
### Narzędzia (w nawiasie przykładowa instalka):
#### 1. SQL Server https://www.microsoft.com/en-us/sql-server/sql-server-editions-express (SQLServer2017-SSEI-Expr i SSMS)
#### 2. MongoDB https://www.mongodb.com/download-center/community (mongodb-win32-x86_64-2008plus-ssl-4.0.10-signed)
#### 3. Robo 3T https://robomongo.org/ (robo3T-1.3.1-windows-x86_64-7419c406)
#### 4. Tableau Desktop https://www.tableau.com/products/desktop/download (TableauDesktop-64bit-2019-2-0)
#### 5. MongoDB BI Connector i ODBC driver https://www.mongodb.com/products/bi-connector (https://info-mongodb-com.s3.amazonaws.com/mongodb-bi/v2/mongodb-bi-win32-x86_64-v2.4.1.msi) i https://github.com/mongodb/mongo-odbc-driver/releases (mongodb-connector-odbc-1.0.0-win-64-bit)
#### 6. Jmeter https://jmeter.apache.org/download_jmeter.cgi (apache-jmeter-5.1.1.zip)
#### 7. Python https://www.python.org/download/releases/ (https://www.python.org/downloads/release/python-2716/)

### Konfiguracja i uruchomienie:
#### 1. Uruchomienie baz danych

##### 1.1 SQL Server - otwórz management studio. Prawym przyciskiem na 'Databases' tworzymy nową bazę, którą nazwiemy 'Economy'. Natępnie otwieramy na tej bazie 'New Query' i tworzymy tabele zapytaniem "Economy.sql".

##### 1.2 MongoDB - uruchom linię poleceń i poleceniem mongod odpal bazę na porcie 20717. Jeśli komenda mongod nie jest rozpoznawalna należy ustawić zmienną środowiskową: 'Panel Sterowania' -> 'System i zabezpieczenia' -> 'System' -> 'Zaawansowane ustawienia systemu' -> 'Zmienne środowiskowe' -> 'Path' i dodajemy ścieżkę do katalogu 'MongoDB\Server\4.0\bin'. Następnie uruchom klienta Robo3T. Utwórz nowe połączenie. W lewym menu na nowo otwartym połączeniu kliknij prawym przyciskiem myszy i stwórz nową bazę "Economy". Rozwiń bazę "Economy" i kliknij następnie prawym przyciskiem na bazę "Collections" i dodaj pierwszą kolekcję "YieldCurve" a następnie kolejną "Recession"

#### 2. Podpięcie Tableau Desktop do SQL Server 

##### 2.1 Uruchom raport "Tableau_YieldCurve_SQLServer.twb". Zostaniesz poproszony o wprowadzenie informacji potrzebnych do połączenia z bazą danych SQL Server. Wzoruj się na załączonym poniżej zrzucie ekranu. Jeśli nie daj Boże pojawi się błąd w stylu Driver's SQLAllocHandle on SQL_HANDLE_ENV Failed, oznacza to ni mniej ni więcej niekompatybilność SQL Server z SQL Server ODBC driver. Doinstaluj odpowiednią wersję.

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

##### 4.2 Będąc w katalogu "rest" wykonaj komendę "python api.py". Pojawią się błędy wynikające z niezainstalowanych bibliotek, które są wykorzystywane przez API. Doinstaluj je używając komendy "pip", w ten sam sposób co powyżej. Instalujemy brakujące biblioteki do skutku :)


## ZAŁADOWANIE DANYCH

#### 1. MongoDB

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/MongoConsole_ImportData.PNG)

#### 2. SQL Server

![Dashboard](https://github.com/przemastro/performance-testing-training-polish/blob/master/SQLServer_Wizard.PNG)

Przykład:
 INSERT INTO YieldCurve(ObservationDate, ObservationDateByMinute, T10Y3M, T10Y2Y) 
 SELECT [Column 0], [Column 1], [Column 2], [Column 3] FROM [dbo].[oneMillionTestData-1]

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
