from twython import Twython
import markovify
import os

# Set these values
APP_KEY = os.environ['CONSUMER_KEY'] 
APP_SECRET = os.environ['CONSUMER_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

longstring = ''''''

#goes through results and print out the actual tweet
results = twitter.search(q='AltRightStarWars', count=300)
for result in results['statuses']:
    longstring += result['text']
    
text_model = markovify.Text(longstring)

for i in range(1, 10):
    print text_model.make_short_sentence(140)
