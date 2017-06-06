import app.texto as texto
import app.twitter as twitter
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
        listagem.append({'text':item,"size":count[item]})
    return listagem



