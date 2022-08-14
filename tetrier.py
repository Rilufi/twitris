from auth import api, api_cor, api_naso, api_gato
import random
import sys

toReply = api.me().screen_name
commands = ['⬅️', '➡️', '⤴️', '⬇️']
bots = [api_cor, api_naso, api_gato]
blocks = ["🟦", "🟥", "🟨", "🟧", "🟪", "🟩", "🟫"]
tweet = api.user_timeline(screen_name=toReply, count=1, exclude_replies = True,  tweet_mode = 'extended')

def tetris(api):
    chosen = random.choice(commands)
    mystring = f""" {chosen}"""
    try:
        api.create_favorite(tweet.id)
        api.update_status("@" + toReply + mystring, in_reply_to_status_id = tweet.id)
    except:
        print(api.me().screen_name + " já tinha comentado")
        pass


for info in tweet:
	if any(block in info.full_text for block in blocks):
		for bot in bots:
			try:
				tetris(bot)
			except:
				pass
	else:
		sys.exit()
