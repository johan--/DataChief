from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time, urllib2,json

ckey = 'UM2gbjeLUmEdDLNXYC7zoJiJo'
csecret = 'u1AcVym5bUBfvwKnqnvUbdYO5R9JGwH5XX39pLztM02nBToQnO'
atoken = '4116102794-mF42wRq0rduIxNmFJEH9BtDLtrjIVFDlJArpT2U'
asecret = 'KG1nzAWotPLASC7pwp4rbcswUkEElMjoFYBXeKD21N65C'

def sentimentAnalysis(text):
    response = alchemyapi.sentiment("text", text)

    print response

    #print int(response["docSentiment"]['score'])
    return 1


class listener(StreamListener):

    def on_data(self,data):
        try:
            #print data

            tweet = data.split(',"text":')[1].split('","source')[0]
            print tweet
            Sentiment = sentimentAnalysis(tweet)

            #print sentiment
            #saveThis = str(time.time()) + '::' + tweet
            #saveFile = open('twitDB2.csv', 'a')
            #saveFile.write(saveThis)
            #saveFile.write('\n')
            #saveFile.close()


            return True
        except BaseException, e:
            print 'failed on error', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())

#San Francisco
twitterStream.filter(track =["car"],locations=[-122.75,36.8,-121.75,37.8])




