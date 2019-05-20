ECHO OFF
REM cd \Program Files\MongoDB\Server\4.0\bin
For /F "delims=, tokens=1,2,3,4,5" %%G IN (C:\Users\pjag\Desktop\Performance\StagingArea\YieldCurveView.csv) DO (
   mongo 127.0.0.1:27017/Economy -u pjag -p admin --eval "db.YieldCurve.insert({'ObservationDate': '%%G', 'T10Y3M': %%H, 'T10Y2Y': %%I, 'Trend_T10Y3M': %%J, 'Trend_T10Y2Y': %%K});"
)