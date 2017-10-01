import app.texto as texto
import app.twitter as twitter
import app.mongo_database as mongo
import app.redis_database as rd
from collections import Counter
from textblob import TextBlob as tb
import numpy as np


def buscarTermo(termo):
    lista = list()
    bons = 0
    ruins = 0
    medios = 0
    analysis = None
    twitts = twitter.buscar(termo)
    for twitt in twitts:
        palavras = texto.limparTexto(twitt.text)
        lista = lista + palavras.split()
        analysis = tb(twitt.text)
        if analysis.sentiment.polarity > 0:
            bons += 1
        else:          
            ruins +=1
    count  = Counter(lista)

    listagem = list()
    sentimento = list()
    sentimento.append({'bons':bons,'ruins':ruins,'media':np.mean(analysis.sentiment.polarity)})

    for item in count:
        listagem.append({'text':item,"size":count[item],"repeticao":count[item]})
    id = mongo.salvar(termo,listagem,sentimento)
    rd.salvar(termo,id)
    retorno = {'resultados':listagem,'sentimento':sentimento}
    return retorno

def verificar(termo):
    id = rd.checar(termo)
    print(id)
    if(id):
        dados = mongo.recuperar(id)
        return dados
    else:
        return buscarTermo(termo)

def recentes():
    return rd.recentes()
