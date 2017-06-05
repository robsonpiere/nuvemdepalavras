import redis

r = redis.StrictRedis(host='', port=0, password='')

def checar(termo):
    if r.exists(termo):
        return r.get(termo)
    else:
        return False

def salvar(termo,valor):
    r.set(termo,valor)