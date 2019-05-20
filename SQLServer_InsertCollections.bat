ECHO OFF
SET SQLCMD="C:\Program Files\Microsoft SQL Server\110\Tools\Binn\SQLCMD.EXE"
REM SET PATH="C:\Users\pjag\Desktop\run_query.sql"
SET SERVER="localhost\SQLEXPRESS"
SET DB="Economy"

REM SET INPUT="C:\Users\pjag\Desktop\run_query.sql"
SET QUERY="INSERT INTO [dbo].[YieldCurve](ObservationDate, T10Y3M, T10Y2Y) VALUES($(ObservationDate), $(T10Y3M), $(T10Y2Y))"

For /F "delims=, tokens=1,2,3,4,5" %%G IN (C:\Users\pjag\Desktop\Performance\StagingArea\YieldCurveView.csv) DO (
   REM mongo 127.0.0.1:27017/Economy -u pjag -p admin --eval "db.YieldCurve.insert({'ObservationDate': '%%G', 'T10Y3M': %%H, 'T10Y2Y': %%I, 'Trend_T10Y3M': %%J, 'Trend_T10Y2Y': %%K});"
   ECHO Success
   %SQLCMD% -S %SERVER% -d %DB% -Q "INSERT INTO [dbo].[YieldCurve](ObservationDate, T10Y3M, T10Y2Y) VALUES('%%G', '%%H', '%%I')"
)