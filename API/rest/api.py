from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from jsonBuilder import getSQLServerData, getSQLServerComplexData, getMongoDBData, getMongoDBComplexData
import ConfigParser
from threading import *
from bson import json_util


app = Flask(__name__)
api = Api(app)


config = ConfigParser.RawConfigParser()
config.read('../resources/env.properties')
serverAddress = config.get('Server', 'server.address')
serverPort = int(config.get('Server', 'server.port'))
serverService = config.get('Server', 'server.service')

class Get_MongoDBData(Resource):
    def get(self):
        data = getMongoDBData()
        return json_util.dumps(data)

class Get_MongoDBComplexData(Resource):
    def get(self):
        data = getMongoDBComplexData()
        return json_util.dumps(data)        

class Get_SQLServerData(Resource):
    def get(self):
        data = getSQLServerData()
        return jsonify(data)

class Get_SQLServerComplexData(Resource):
    def get(self):
        data = getSQLServerComplexData()
        return jsonify(data)        

api.add_resource(Get_MongoDBData, '/getMongoDBData')
api.add_resource(Get_MongoDBComplexData, '/getMongoDBComplexData')
api.add_resource(Get_SQLServerData, '/getSQLServerData')
api.add_resource(Get_SQLServerComplexData, '/getSQLServerComplexData')


# Handling COR requests
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,SessionId,Email')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    response.headers.add("Access-Control-Max-Age", "3600");
    response.headers.add("Access-Control-Allow-Headers", "x-requested-with");
    response.headers.add("Connection", "keep-alive");
    response.headers.add("Vary", "Accept-Encoding");
    return response


if __name__ == '__main__':
    app.run(debug=False, host=serverAddress, port=serverPort, threaded=True, use_reloader=True)

