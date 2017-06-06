import pymongo
from pymongo import MongoClient

cliente = MongoClient('***REMOVED***')
db = cliente.nuvempalavras #define database used

teste = db.teste

#teste 
import pprint
for item in teste.find():
    pprint.pprint(item)