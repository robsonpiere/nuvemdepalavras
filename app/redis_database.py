import redis
import os

HOST_REDIS = os.environ.get('HOST_REDIS')
PORT_REDIS = os.environ.get('PORT_REDIS')
PASSWORD_REDIS = os.environ.get('PASSWORD_REDIS')

#substituir por variaveis de ambiente
r = redis.StrictRedis(host=HOST_REDIS, port=PORT_REDIS, password=PASSWORD_REDIS,charset="utf-8", decode_responses=True)

def checar(termo):
    if r.exists(termo):
        return r.get(termo)
    else:
        return False

def salvar(termo,valor):
    r.set(termo,valor,ex=300)

def recentes():
    return r.keys()