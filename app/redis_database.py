import redis

#substituir por variaveis de ambiente
r = redis.StrictRedis(host='***REMOVED***', port=18605, password='***REMOVED***')

def checar(termo):
    if r.exists(termo):
        return r.get(termo)
    else:
        return False

def salvar(termo,valor):
    r.set(termo,valor)