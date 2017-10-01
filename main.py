from flask import Flask
from flask import request
from flask import render_template
import app.contador as cont

app = Flask(__name__)

@app.route('/')
def exemplo():
  lista = [{'text':'Palavras','size':40,'repeticao':40},{'text':'Sentimento','size':20,'repeticao':20},{'text':'Nuvem','size':17,'repeticao':17},{'text':'Recuperação','size':10,'repeticao':10},{'text':'Informação','size':15,'repeticao':15},{'text':'twitter','size':9,'repeticao':9}]
  sentimento = [{'bons':50,'ruins':50,'media':0.15}]
  return render_template('index.html',valores=lista,termo="Palavras",sentimento=sentimento)

@app.route('/sobre')
def sobre():
  integrantes = ["Robson Piere"]
  return render_template('sobre.html',integrantes=integrantes)

@app.route('/recentes')
def recentes():
  recentes = cont.recentes()
  return render_template('recentes.html',recentes=recentes)

@app.route('/buscar/<termo>',methods=['GET', 'POST'])
def busca(termo=''):
  busca = cont.verificar(termo)
  palavras = busca['resultados']
  sentimento = busca['sentimento']
  return render_template('index.html',valores=palavras,termo=termo,sentimento=sentimento)


if __name__ == '__main__':
  app.run()