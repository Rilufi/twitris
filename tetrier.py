from auth import api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato
import random

toReply = "rilufix"


commands = ['⬅️', '➡️', '⤴️', '⬇️']


def tetris(api):
	tweets = api.user_timeline(screen_name = toReply, count=1)
	chosen = random.choice(commands)

	mystring = f""" {chosen}"""
	
	for tweet in tweets:
        	api.update_status("@" + toReply + mystring, in_reply_to_status_id = tweet.id)

tetris(api_xame)
tetris(api_uva)
tetris(api_mevu)
tetris(api_cor)
tetris(api_naso)
tetris(api_gato)