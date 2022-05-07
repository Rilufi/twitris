from auth import api_cor, api_naso, api_gato, api_ril
import random
import sys

commands = ['⬅️', '➡️', '⤴️', '⬇️']
bots = [api_cor, api_naso, api_gato]
blocks = ["🟦", "🟥", "🟨", "🟧", "🟪", "🟩", "🟫"]
tweets = api_ril.user_timeline(screen_name="rilufix", count=1, exclude_replies = True,  tweet_mode = 'extended')

def tetris(api):
	chosen = random.choice(commands)
	mystring = f""" {chosen}"""
	for tweet in tweets:
		api.update_status("@" + "rilufix" + mystring, in_reply_to_status_id = tweet.id)

for info in tweets:
	if any(block in info.full_text for block in blocks):
		for bot in bots:
			try:	
				tetris(bot)
			except:
				pass
	#elif "⬜" or "⬛" in info.full_text:
	#	for bot in bots:
	#		try:	
	#			tetris(bot)
	#		except:
	#			pass
	else:
		sys.exit()
