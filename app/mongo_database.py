import pymongo
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

cliente = MongoClient('mongodb://nuvem:balde@ds111262.mlab.com:11262/nuvempalavras')
db = cliente.nuvempalavras #define database used

def salvar(termo,resultados):
    buscas = db.buscas
    busca = {'termo':termo,'resultados':resultados}
    return buscas.insert_one(busca).inserted_id

def recuperar(identificador):
    buscas = db.buscas
    dados = buscas.find_one({'_id': ObjectId(identificador)})
    return dados