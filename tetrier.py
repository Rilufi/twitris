from auth import api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato
import random
import sys

commands = ['⬅️', '➡️', '⤴️', '⬇️']
bots = [api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato]

def tetris(api):
	tweets = api.user_timeline(screen_name="rilufix", count=1, exclude_replies = True,  tweet_mode = 'extended')
	chosen = random.choice(commands)
	mystring = f""" {chosen}"""
	
	for info in tweets:
		if "ArXiv" not in info.full_text:
			for tweet in tweets:
				api.update_status("@" + "rilufix" + mystring, in_reply_to_status_id = tweet.id)
		else:
			sys.exit()

for bot in bots:
	try:
		tetris(bot)
	except:
		pass
