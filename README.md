# TestingTraining (Polish)
SQL Server + MongoDB + Tableau + Python + Jmeter

Nie za krótkie wprowadzenie do testowania wydajności systemów opartych na bazach relacyjnych i nierelacyjnych.
W tym odcinku porównamy wydajność baz SQLServer i MongoDB korzystając z klienta Tableau i API Flask (Python).

Instalacja:
1. SQL Server
https://www.microsoft.com/en-us/sql-server/sql-server-editions-express
2. MongoDB
https://www.mongodb.com/download-center/community
3. Robo 3T
https://robomongo.org/
4. Tableau Desktop
https://www.tableau.com/products/desktop/download
5. MongoDB BI Connector
https://www.mongodb.com/products/bi-connector
https://medium.com/@marshallma_67148/connect-mongodb-3-4-with-tableau-2018-01-on-window-10-06-2018-496d04e3e969
6. Jmeter
https://jmeter.apache.org/download_jmeter.cgi

Załadowanie danych:
1. Schemat SQL Server
Economy.sql
2. Kolekcje MongoDB
Economy Folder
3. Skrypt ETL-owy
MongoDB_InsertCollections.bat
SQLServer_InsertCollections.bat

Testy i wyniki testów: 

Test Case 0 - Chcemy sprawdzić czasy wykonania zapytań na obu bazach.

| Set        | MongoDB           | SQLServer  |
| ------------- |:-------------:| -----:|
|  1   | |  |
|  2   | |  |
|  3   | |  |
|  4   | |  |
|  5   | |  |


Test Case 1 - Chcemy sprawdzić jak zmieniają się czasy wykonania zapytań na obu bazach przy użyciu Tableau Desktop wraz z ładowaniem danych testowych.

| Set        | MongoDB           | SQLServer  |
| ------------- |:-------------:| -----:|
|  0   | Rendering - Exec Query - DataSource - Layout | Rendering - Exec Query - DataSource - Layout |
|  1   | |  |
|  2   | |  |
|  3   | |  |
|  4   | |  |
|  5   | |  |
|  6   | |  |
|  7   | |  |
|  8   | |  |
|  9   | |  |
|  10  | |  |


Test Case 2 - Chcemy sprawdzić czasy wykonania zapytań na obu bazach przy użyciu Tableau Desktop po założeniu indeksów.

| Set        | MongoDB           | SQLServer  |
| ------------- |:-------------:| -----:|
|  0   | Rendering - Exec Query - DataSource - Layout | Rendering - Exec Query - DataSource - Layout |
|  1   | |  |


Test Case 3 - Chcemy sprawdzić czasy wykonania zapytań na obu bazach przy użyciu Tableau Desktop po połączniu głównej tabeli z kolejną tabelą.

| Set        | MongoDB           | SQLServer  |
| ------------- |:-------------:| -----:|
|  0   | Rendering - Exec Query - DataSource - Layout | Rendering - Exec Query - DataSource - Layout |
|  1   | |  |


Test Case 4 - Chcemy sprawdzić czasy wykonania zapytań na obu bazach przy użyciu Tableau Desktop po zastosowaniu SQL "Hint-ów" i MongoDB "Hintów" .

| Set        | MongoDB           | SQLServer  |
| ------------- |:-------------:| -----:|
|  0   | Rendering - Exec Query - DataSource - Layout | Rendering - Exec Query - DataSource - Layout |
|  Hint 1   | |  |
|  Hint 2   | |  |
|  Hint 3   | |  |


Test Case 5 - Chcemy sprawdzić czasy wykonania zapytań na obu bazach przy użyciu Flask API dla małego i dużego ruchu.

| Set        | MongoDB           | SQLServer  |
| ------------- |:-------------:| -----:|
|  0   |  | |
|  Mały ruch   | |  |
|  Duży ruch   | |  |
