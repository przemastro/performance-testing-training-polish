##MongoDB test data import

###mongoimport --jsonArray --db Economy --collection YieldCurve --file YieldCurveTestData-1.json

###mongoimport --jsonArray --db Economy --collection Recession --file RecessionTestData.json
 
###mongoimport --jsonArray --db Economy --collection YieldCurve --file YieldCurveTestData_9000.json

###mongoimport --jsonArray --db Economy --collection Recession --file RecessionTestData_9000.json

##SQL Server test data import 

###INSERT INTO YieldCurve(ObservationDate, ObservationDateByMinute, T10Y3M, T10Y2Y) SELECT [Column 0], [Column 1], [Column 2], [Column 3] FROM [dbo].[YieldCurveTestData-4]

###INSERT INTO Recession(ObservationDate, ObservationDateByMinute, Recession) SELECT [Column 1], [Column 2], [Column 3] FROM [dbo].[RecessionTestData]


##Counts

###db.YieldCurve.count(); 

###Select count(*) from YieldCurve
