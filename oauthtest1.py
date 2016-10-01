from twython import Twython
import markovify
import os

# Set these values
APP_KEY = os.environ['CONSUMER_KEY'] 
APP_SECRET = os.environ['CONSUMER_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

toronto = twitter.get_place_trends(id=2487956)
trend_array = []
if toronto:
   for trend in toronto[0].get('trends', []):
      trend_array.append(trend['name'])

#print trend_array
longstring = ''''''

search = trend_array[0]
search = search[1:]

#print search 

#goes through results and print out the actual tweet
results = twitter.search(q=search, count=300)
for result in results['statuses']:
    longstring += result['text']
    
text_model = markovify.Text(longstring)

twitter.update_status(status=text_model.make_short_sentence(140))

