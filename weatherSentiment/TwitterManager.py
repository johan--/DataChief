from alchemyapi import AlchemyAPI
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time, datetime
import pandas as pd
from models import Tweet

class TwitterManager(StreamListener):
    def on_data(self, data):
        try:
            tweet = data.split(',"text":')[1].split('","source')[0]
            print data
            print tweet
            sentiment = TwitterManager.sentiment_analysis(tweet)
            TwitterManager.save_data_to_database(data, tweet, sentiment)
            time.sleep(5)
            return True
        except BaseException, e:
            print 'failed on error', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

    @staticmethod
    def start_stream(locations):
        ckey = 'CM5GrRbDPL8IYdmYaYR2xmaDj'
        csecret = 'bBTb6vSLFKMjE4SSBMjfVEqgyc3DDvwt6DtAK0BITOiUy7V76Y'
        atoken = '2587929073-sF7e5rjf0kkjuSc2ULMzeMQg6GS6V1fY95ccebF'
        asecret = 'EVUypMV5dZKYn7Ro2hD9DHDufAZFVf698qzUbqNYJDIQX'
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitter_stream = Stream(auth, TwitterManager())
        twitter_stream.filter(track =["weather"],locations=[-122.75,36.8,-121.75,37.8])

    @staticmethod
    def sentiment_analysis(text):
        alchemy_api = AlchemyAPI()
        response = alchemy_api.sentiment("text", text)
        try:
            float(response["docSentiment"]['score'])
            return float(response["docSentiment"]['score'])
        except ValueError:
            return None

    def save_data_to_database(twitter_data, tweet, sentiment):
        # tweet = Tweet(message=tweet, sentiment=sentiment, datetime=datetime.datetime.now())
        # tweet.save()
        return 1
