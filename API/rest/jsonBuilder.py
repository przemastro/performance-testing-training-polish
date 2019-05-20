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
            data.insert(3, x[2])
            data.insert(4, x[3]) 
            data.insert(5, x[4])  
        return data
    except:
        print 'errors in getSQLServerData function'
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


