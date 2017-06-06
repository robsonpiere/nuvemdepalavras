from flask import Flask
from flask import request
from flask import render_template
import app.contador as cont

app = Flask(__name__)

@app.route('/')
def exemplo():
  lista = [{'text':'Mateuzim','size':40},{'text':'Nada','size':20},{'text':'Vale','size':17},{'text':'Value=0','size':10}]
  return render_template('index.html',valores=lista)

@app.route('/sobre')
def sobre():
  integrantes = ["Mateus Fernando","Mirlaine Ribeiro","Robson Piere","Yitzhak Andrade"]
  return render_template('sobre.html',integrantes=integrantes)

@app.route('/busca/<termo>')
def busca(termo=''):
  palavras = cont.verificar(termo)
  return render_template('index.html',valores=palavras)


if __name__ == '__main__':
  app.run()