
#Import the necessary methods from tweepy library
import tweepy
from tweepy import OAuthHandler
import json
import os
import time

#get keys from: https://apps.twitter.com/
#consumer key, consumer secret, access token, access secret.
ckey = '9D2w3iTfxI4bTzFeOc614d86l'
csecret = 'DCOGCqDrahobYeB9oOHD0VYuOL5PH8PnWTXEkbGL9OhZpuc5lQ'
atoken = '955940903658631168-kL0fVS7uk6bn1KCBkbQ3oIZn9v23OGS'
asecret = 'XbYHSyrVZSLEatrk3IVs23ScEWi2vPu2825g44aOJHARf'
f = open("TwitterCount.txt", "w+")
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api=tweepy.API(auth, wait_on_rate_limit=True)
ids = []
user = api.get_user('acnwala')
print(user.screen_name)
for page in tweepy.Cursor(api.followers_ids, screen_name="acnwala").pages():
    ids.extend(page)
for i in ids:
    u = api.get_user(i)
    print(u.screen_name + " " + str( u.followers_count))
    f.write(u.screen_name+","+str(u.followers_count)+"\n")
