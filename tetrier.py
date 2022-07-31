from auth import api, api_cor, api_naso, api_gato
import random
import sys

commands = ['⬅️', '➡️', '⤴️', '⬇️']
bots = [api_cor, api_naso, api_gato]
blocks = ["🟦", "🟥", "🟨", "🟧", "🟪", "🟩", "🟫"]
tweets = api.user_timeline(screen_name=api.me().screen_name, count=1, exclude_replies = True,  tweet_mode = 'extended')

def tetris():
	chosen = random.choice(commands)
	mystring = f""" {chosen}"""
	for tweet in tweets:
		api_naso.update_status("@" + "botoronga" + mystring, in_reply_to_status_id = tweet.id)
		api_gato.update_status("@" + "botoronga" + mystring, in_reply_to_status_id = tweet.id)

for info in tweets:
	if any(block in info.full_text for block in blocks):
		try:	
			tetris()
		except:
			pass
	else:
		sys.exit()
