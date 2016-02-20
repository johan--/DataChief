from alchemyapi import AlchemyAPI
alchemyapi = AlchemyAPI()
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import time, urllib2, json
import pandas as pd

ckey = 'UM2gbjeLUmEdDLNXYC7zoJiJo'
csecret = 'u1AcVym5bUBfvwKnqnvUbdYO5R9JGwH5XX39pLztM02nBToQnO'
atoken = '4116102794-mF42wRq0rduIxNmFJEH9BtDLtrjIVFDlJArpT2U'
asecret = 'KG1nzAWotPLASC7pwp4rbcswUkEElMjoFYBXeKD21N65C'

def sentimentAnalysis(text):
    response = alchemyapi.sentiment("text", text)
    #print int(response["docSentiment"]['score'])
    return 1













class listener(StreamListener):

    def on_data(self,data):
        try:

            tweet = data.split(',"text":')[1].split('","source')[0]
            print data
            print tweet
            Sentiment = sentimentAnalysis(tweet)
            time.sleep(5)

            return True
        except BaseException, e:
            print 'failed on error', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())


#Get cities from saved data
coordinates_dict_twitter = {}
coordinates_dict_weather = []

file = open('cities.csv', 'r')
temp_list = []
dataframe = pd.read_csv(file)

def geobox(place):
    geobox = []
    geobox.append(place[1] - .5)
    geobox.append(place[0] - .5)
    geobox.append(place[1] + .5)
    geobox.append(place[0] + .5)
    return geobox

def get_coordinates(file):
    for x in range(0,int(dataframe['city'].count())):
        temp_weather = []
        temp_list.append(dataframe['lat'][x])
        temp_list.append(dataframe['lng'][x])
        temp_weather.append(dataframe['state'][x])
        temp_weather.append(dataframe['city'][x])
        coordinates_dict_twitter[dataframe['city'][x]] = geobox(temp_list)
        temp_list[:] = []
        coordinates_dict_weather.append(temp_weather)

get_coordinates(file)
coordinates_dict_twitter

weather_base =  'http://api.wunderground.com/api/e1fde55153190b2a/geolookup/conditions/q/'


def compile_data(coordinates_dict_twitter, coordinates_dict_weather):
    state = coordinates_dict_weather[0][0]
    city = coordinates_dict_weather[0][1]
    extension = state + '/' + city + '.json'
    weather_full = weather_base + extension
    weather_run(weather_full)


def weather_run(weather_full):

    # Weather underground api calls
    f = urllib2.urlopen(weather_full)
    json_string = f.read()
    parsed_json = json.loads(json_string)
    print parsed_json['current_observation']
    print parsed_json['current_observation']['precip_today_in']
    print parsed_json['current_observation']['feelslike_f']
    print parsed_json['current_observation']['weather']


compile_data(coordinates_dict_twitter, coordinates_dict_weather)


#San Francisco
#twitterStream.filter(locations=cities['location'])



