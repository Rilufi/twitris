from auth import api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato
import random

toReply = "rilufix"

commands = ['⬅️', '➡️', '⤴️', '⬇️']

bots = ['api_xame', 'api_uva', 'api_mevu', 'api_cor', 'api_naso', 'api_gato']

def tetris(api):
	tweets = api.user_timeline(screen_name = toReply, count=1)
	chosen = random.choice(commands)

	mystring = f""" {chosen}"""
	
	for tweet in tweets:
        	api.update_status("@" + toReply + mystring, in_reply_to_status_id = tweet.id)

for bot in bots:
    tetris(bot)
