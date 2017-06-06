import pymongo
from pymongo import MongoClient

cliente = MongoClient('mongodb://nuvem:balde@ds111262.mlab.com:11262/nuvempalavras')
db = cliente.nuvempalavras #define database used

teste = db.teste

#teste 
import pprint
for item in teste.find():
    pprint.pprint(item)