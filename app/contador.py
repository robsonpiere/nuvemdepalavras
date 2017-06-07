import app.texto as texto
import app.twitter as twitter
import app.mongo_database as mongo
import app.redis_database as rd
from collections import Counter


def buscarTermo(termo):
    lista = list()
    twitts = twitter.buscar(termo)
    for twitt in twitts:
        palavras = texto.limparTexto(twitt.text)
        lista = lista + palavras.split()
    count  = Counter(lista)

    listagem = list()

    for item in count:
        listagem.append({'text':item,"size":count[item],"repeticao":count[item]})
    id = mongo.salvar(termo,listagem)
    rd.salvar(termo,id)
    return listagem

def verificar(termo):
    id = rd.checar(termo)
    print(id)
    if(id):
        dados = mongo.recuperar(id)
        return dados['resultados']
    else:
        return buscarTermo(termo)

def recentes():
    return rd.recentes()
