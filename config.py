# Database connection
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb+srv://username:password@cluster0.8ug6g.mongodb.net/?appName=Cluster0'

#Create a new client and conenct to the server
client = MongoClient(uri, server_api = ServerApi('1'))

#create database 
db = client['userDb']

#create collection/table
collection = db['user']
