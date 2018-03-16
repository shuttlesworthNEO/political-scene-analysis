import pandas as pd
import os.path
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret
ckey="#"
csecret="#"
atoken="#"
asecret="#"

class listener(StreamListener):

	def on_data(self, data):
		dataDic = json.loads(data)
		print(dataDic)
		try:
			text = str(dataDic['text'])
		except:
			text = ''

		if(len(text) != 0):

			temp = {
				"id" : dataDic["id"],
				"text" : text
			}
			df = pd.DataFrame(data=temp, index=[0])
			if(os.path.exists('data/test.csv')):
				with open('data/test.csv', 'a') as f:
					df.to_csv(f, header=None, index=None)
			else:
				with open('data/test.csv', 'a') as f:
					df.to_csv(f, index=None)
		# saveFile = open("twitDB.csv", 'a')
		# saveFile.write(str(dataDic["id"]))
		# saveFile.write(',')
		# saveFile.write(str(dataDic['text'].encode('utf-8')))
		# saveFile.write('\n')
		# saveFile.close()
		return(True)

	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["BJP"])

