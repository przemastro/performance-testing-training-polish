import pyodbc
import ast
import ConfigParser
import pymongo
from pymongo import MongoClient

config = ConfigParser.RawConfigParser()
config.read('../resources/env.properties')
dbAddress = config.get('DatabaseConnection', 'database.address')
cnx = pyodbc.connect(dbAddress)
cursor = cnx.cursor()


def getSQLServerData():
    try:
        getSQLServerData = "SELECT * FROM [dbo].[YieldCurve]"
        data = []
        cursor.execute(getSQLServerData)
        value = cursor.fetchall()
        for x in value:
            data.insert(1, x[0])
            data.insert(2, x[1])
            #data.insert(3, x[2])
            data.insert(4, float(x[3])) 
            data.insert(5, float(x[4]))  
        return data
    except:
        print 'errors in getSQLServerData function'
    else:
        cnx.close()

def getSQLServerComplexData():
    try:
        getSQLServerData = ("SELECT yc.Id as ID, yc.ObservationDate as ObservationDate, yc.T10Y3M, yc.T10Y2Y, re.Recession " 
            "FROM [dbo].[YieldCurve] yc LEFT JOIN [dbo].[Recession] re ON yc.ObservationDate = re.ObservationDate")
        data = []
        cursor.execute(getSQLServerData)
        value = cursor.fetchall()
        for x in value:
            data.insert(1, x[0])
            data.insert(2, x[1])
            data.insert(3, float(x[2])) 
            data.insert(4, float(x[3]))  
            data.insert(5, x[4])
        return data
    except:
        print 'errors in getSQLServerComplexData function'
    else:
        cnx.close()

def getMongoDBData():
    try:
        myclient = MongoClient('localhost',27017)
        mydb = myclient["Economy"]
        mycoll=mydb["YieldCurve"]
        data = []
        for x in mycoll.find():
           data.append(x)
        return data   
    except:
        print 'errors in getMongoDBData function'
    else:
        myclient.close() 

def getMongoDBComplexData(): 
    try:
        myclient = MongoClient('localhost',27017)
        mydb = myclient["Economy"]
        mycoll=mydb.YieldCurve.aggregate([
            {"$lookup":  
              { 
                "from": "Recession",
                "localField": "ObservationDate",
                "foreignField": "ObservationDate", 
                "as": "Recession"
              }
            }
        ]) 
        data = []
        for x in mycoll:
           data.append(x)
        return data  
    except:
        print 'errors in getMongoDBComplexData function'
    else:
        myclient.close()                


