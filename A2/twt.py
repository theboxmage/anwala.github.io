'''
        prerequisites:
        0. create a twitter account
        1. obtain your access tokens: https://apps.twitter.com/
                1.0 create new app
        2. install tweepy (pip install tweepy)

        credit:
        http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html
        http://adilmoujahid.com/posts/2014/07/twitter-analytics/
        https://pythonprogramming.net/twitter-api-streaming-tweets-python-tutorial/

        Tweet JSON:, use http://jsonviewer.stack.hu/ to view object
        https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json

        rate limiting:
        https://developer.twitter.com/en/docs/basics/rate-limiting

        streaming rate limiting:
        https://developer.twitter.com/en/docs/tweets/filter-realtime/guides/connecting.html
'''

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import time
import requests

#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey = '9D2w3iTfxI4bTzFeOc614d86l'
csecret = 'DCOGCqDrahobYeB9oOHD0VYuOL5PH8PnWTXEkbGL9OhZpuc5lQ'
atoken = '955940903658631168-kL0fVS7uk6bn1KCBkbQ3oIZn9v23OGS'
asecret = 'XbYHSyrVZSLEatrk3IVs23ScEWi2vPu2825g44aOJHARf'
#
URIs={}
class listener(StreamListener):

        def on_data(self, data):
                #learn about tweet json structure: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
                try:
                    tweetJson = json.loads(data)

                #tweet = tweetJson['text']
                    username = tweetJson['user']['screen_name']
                    links = tweetJson['entities']['urls']
                except:
                    return True
                if( len(links) != 0 and tweetJson['truncated'] == False ):
                        links = self.getLinksFromTweet(links)

                        print( username )
                        for l in links:
                            try:
                                r = requests.head(l, allow_redirects=True, timeout=10)
                                if( r.status_code > 199 and r.status_code < 300):
                                    print(r.history)
                                    print('\t', r.url)
                                    if 'https://twitter'  not in r.url:
                                        URIs[r.url] = r.history
                            except:
                                return True
                        print ()
                        print(len(URIs))
                        print()
                        if len(URIs) > 1000:
                            f = open('test','a')
                            for key, value in URIs.items():
                                f.write(key + '\n')
                                print(key)
                            return False
                #time.sleep(5)

                return True
        def getLinksFromTweet(self, linksDict):
                links = []
                for uri in linksDict:
                        links.append( uri['expanded_url'] )

                return links

        def on_error(self, status):
                print( status )

                if status == 420:
                        #returning False in on_data disconnects the stream
                        return False
                return True


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
while( len(URIs) < 1000):
    try:
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=['olympics'])
    except:
        pass
