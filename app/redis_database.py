import redis

#substituir por variaveis de ambiente
r = redis.StrictRedis(host='***REMOVED***', port=18605, password='***REMOVED***',charset="utf-8", decode_responses=True)

def checar(termo):
    if r.exists(termo):
        return r.get(termo)
    else:
        return False

def salvar(termo,valor):
    r.set(termo,valor,ex=60)

def recentes():
    return r.keys()