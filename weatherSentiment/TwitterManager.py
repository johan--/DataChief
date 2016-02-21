from alchemyapi import AlchemyAPI
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time, urllib2, json
import pandas as pd
from models import Tweet


class TwitterManager(StreamListener):
    def on_data(self, data):
        try:
            tweet = data.split(',"text":')[1].split('","source')[0]
            print data
            print tweet
            Sentiment = TwitterManager.sentiment_analysis(tweet)
            time.sleep(5)
            return True
        except BaseException, e:
            print 'failed on error', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

    @staticmethod
    def start_stream(locations):
        c_key = 'UM2gbjeLUmEdDLNXYC7zoJiJo'
        c_secret = 'u1AcVym5bUBfvwKnqnvUbdYO5R9JGwH5XX39pLztM02nBToQnO'
        a_token = '4116102794-mF42wRq0rduIxNmFJEH9BtDLtrjIVFDlJArpT2U'
        a_secret = 'KG1nzAWotPLASC7pwp4rbcswUkEElMjoFYBXeKD21N65C'
        auth = OAuthHandler(c_key, c_secret)
        auth.set_access_token(a_token, a_secret)
        twitter_stream = Stream(auth, TwitterManager())
        twitter_stream.firehose()

    def sentiment_analysis(text):
        alchemy_api = AlchemyAPI()
        response = alchemy_api.sentiment("text", text)
        # print int(response["docSentiment"]['score'])
        return 1