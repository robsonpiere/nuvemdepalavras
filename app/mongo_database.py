import pymongo
import datetime
import os
from pymongo import MongoClient
from bson.objectid import ObjectId


HOST_MONGO = os.environ.get('HOST_MONGO')

cliente = MongoClient(HOST_MONGO)
db = cliente.nuvempalavras #define database used

def salvar(termo,resultados,sentimento):
    buscas = db.buscas
    busca = {'termo':termo,'resultados':resultados,'sentimento':sentimento, 'createdAt':datetime.datetime.utcnow()}
    return buscas.insert_one(busca).inserted_id

def recuperar(identificador):
    buscas = db.buscas
    dados = buscas.find_one({'_id': ObjectId(identificador)})
    return dados