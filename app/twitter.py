import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def buscar(termo):
    api = tweepy.API(auth)
    results = api.search(q=termo,lang='pt-br')
    for result in results:
        print (result.text)