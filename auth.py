import tweepy
import os

#Rilufi

consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN_KEY"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api_ril = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


#Xamexavu

consumer_key = os.environ["CONSUMER_KEY_XAME"]
consumer_secret = os.environ["CONSUMER_SECRET_XAME"]
access_token = os.environ["ACCESS_TOKEN_XAME"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_XAME"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api_xame = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

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


#Mevuxa

consumer_key = os.environ["CONSUMER_KEY_MEVU"]
consumer_secret = os.environ["CONSUMER_SECRET_MEVU"]
access_token = os.environ["ACCESS_TOKEN_MEVU"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_MEVU"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_mevu = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)



#Uvaxemax


consumer_key = os.environ["CONSUMER_KEY_UVA"]
consumer_secret = os.environ["CONSUMER_SECRET_UVA"]
access_token = os.environ["ACCESS_TOKEN_UVA"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_UVA"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Controls Twitter account
api_uva = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)
