# :cloud: Nuvem de palavras  :cloud:

Trabalho apresentado para matéria do curso de banco de dados não relacionais do curso de pós graduação em Ciência de dados e Big data - Puc Minas 2017

A busca é efetuada no [Twitter](https://twitter.com/) (100 twitts) e monta uma de palavras com os termos que aparecem na busca.  :shipit:  :mag:

Exemplo no Azure [http://nuvemdepalavras.azurewebsites.net](http://nuvemdepalavras.azurewebsites.net)

Exemplo no Heroku [https://nuvemdepalavras.herokuapp.com/](https://nuvemdepalavras.herokuapp.com/)

## Membros do grupo
 - Mateus Fernando [@mfpinheiro](https://github.com/mfpinheiro)
 - Mirlaine Ribeiro [@Mirlaine](https://github.com/Mirlaine)
 - Robson Piere [@robsonpiere](https://github.com/robsonpiere/)
 - Yitzhak Andrade[@YitzhakAndrade](https://github.com/YitzhakAndrade)
 
 - Professor Henrique Batista

## links

- [Site publicado no Heroku](https://nuvemdepalavras.herokuapp.com/)

- [Plugin d3](https://d3js.org/)

- [Plugin word cloud d3 - @jasondavies](https://github.com/jasondavies/d3-cloud)

- [Plugin modificado(layout) por @wvengen](https://github.com/wvengen/d3-wordcloud)

- [Mongo DB free - Mlab](https://mlab.com/)

- [Redis Free - Redis Labs](https://redislabs.com/)

## Como rodar o projeto

### Necessário
- python 3.x
- Flask
- redis
- tweepy
- pymongo
- gunicorn (para deploy no [Heroku](https://www.heroku.com/))

### Configurar as variáveis de ambiente (ou informar no código)

- Redis 
  - HOST_REDIS 
  - PORT_REDIS
  - PASSWORD_REDIS

- Mongodb
  - HOST_MONGO

- API Twitter
  - CONSUMER_KEY
  - CONSUMER_SECRET
  - ACCESS_TOKEN 
  - ACCESS_TOKEN_SECRET

### Executar o projeto

```bash
#Na pasta raiz do projeto:
python main.py
``` 

