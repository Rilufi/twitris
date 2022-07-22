import tweepy
import os


#Botoronga

consumer_key = os.environ["CONSUMER_KEY_COR"]
consumer_secret = os.environ["CONSUMER_SECRET_COR"]
access_token = os.environ["ACCESS_TOKEN_COR"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_COR"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api_cor = tweepy.API(auth)


#Gato

consumer_key = os.environ["CONSUMER_KEY_GATO"]
consumer_secret = os.environ["CONSUMER_SECRET_GATO"]
access_token = os.environ["ACCESS_TOKEN_GATO"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_GATO"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api_gato = tweepy.API(auth)


#Nasa

consumer_key = os.environ["CONSUMER_KEY_NASO"]
consumer_secret = os.environ["CONSUMER_SECRET_NASO"]
access_token = os.environ["ACCESS_TOKEN_NASO"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_NASO"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api_naso = tweepy.API(auth)
