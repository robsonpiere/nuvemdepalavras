import tweepy

#substituir por variaveis de ambiente
auth = tweepy.OAuthHandler('EL5gitP9VX02DHc57SEeyVGV3', 'O3qWLijPYEv1o5ZISl7cpCKfIQqz1Y5XkkjMdz3z6knnzuj8Hl')
auth.set_access_token('133379539-VklLN3OkcsABHNLa06P6XZG1sBLhE0OZfglBNAi8','Xjoudeyd4dF9Mikgd5kkvKBbAQU0t2eBzblYtg6YNIuma')

def buscar(termo):
    api = tweepy.API(auth)
    results = api.search(q=termo,lang='pt-br',count=100)
    return results