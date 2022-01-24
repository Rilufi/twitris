from auth import api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato, api_ril
import random
import sys

commands = ['⬅️', '➡️', '⤴️', '⬇️']
bots = [api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato]
tweets = api_ril.user_timeline(screen_name="rilufix", count=1, exclude_replies = True,  tweet_mode = 'extended')

def tetris(api):
	chosen = random.choice(commands)
	mystring = f""" {chosen}"""
	for tweet in tweets:
		api.update_status("@" + "rilufix" + mystring, in_reply_to_status_id = tweet.id)

for bot in bots:
	try:
		for info in tweets:
			if "⬜" in info.full_text:
				tetris(bot)
			elif "⬛" in info.full_text:
				tetris(bot)
			else:
				sys.exit()
	except:
		pass
