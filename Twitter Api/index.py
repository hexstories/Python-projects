import tweepy
from tweepy import OAuthHandler
 
consumer_key = '8Dclw7DfxIThL8uxv4mvJRARF'
consumer_secret = 'EPr6iJiN1VA5D28VjpnM4hwjwNdFiTrQBmpOEFhVuQKTFHr4wK'
access_token = '970852111163494401-7IzNnaFBAHFjN2k3Ocm3UDAekGXJzw1'
access_secret = 'UpUO1z6C6HS1Z3SEfnpCz6swibQO3itq0WlKYx1CgbIKz'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)  # Process a single status
