import redis

#substituir por variaveis de ambiente
r = redis.StrictRedis(host='redis-18605.c14.us-east-1-3.ec2.cloud.redislabs.com', port=18605, password='balde')

def checar(termo):
    if r.exists(termo):
        return r.get(termo)
    else:
        return False

def salvar(termo,valor):
    r.set(termo,valor)