from twython import Twython

import os

# Set these values
APP_KEY = os.environ['CONSUMER_KEY'] 
APP_SECRET = os.environ['CONSUMER_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

print "twitter = "
print twitter

ACCESS_TOKEN = twitter.obtain_access_token()

print "access token is: "
print ACCESS_TOKEN

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


result = twitter.search(q='debate')

print result['statuses'][1]

#twitter = Twython(APP_KEY, APP_SECRET,
#                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

