from auth import api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato
import random

commands = ['⬅️', '➡️', '⤴️', '⬇️']
bots = [api_xame, api_uva, api_mevu, api_cor, api_naso, api_gato]
blocks= ["⬛", "⬜", "🟦", "🟥", "🟨", "🟧","🟪","🟩","🟫"]

def tetris(api):
	tweets = api.user_timeline(screen_name = "rilufix", count=1)
	chosen = random.choice(commands)
	mystring = f""" {chosen}"""
	res = [ele for ele in blocks if(ele in tweets)]

	if bool(res) != False:
		for tweet in tweets:
	        	api.update_status("@" + "rilufix" + mystring, in_reply_to_status_id = tweet.id)
	else:
		pass

for bot in bots:
    tetris(bot)
