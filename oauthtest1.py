from twython import Twython
import markovify
import os

# Set these values
APP_KEY = os.environ['CONSUMER_KEY'] 
APP_SECRET = os.environ['CONSUMER_SECRET']
OAUTH_TOKEN = "782061749801320448-mCvd8o35dEZ2rcRmx7EOKbUS1fRMItg"
OAUTH_TOKEN_SECRET = "VOD7LLtb1AoNQBPL4DT7ihLf7EfYQ7YIishBiWFMK6MQN"

#twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

#ACCESS_TOKEN = twitter.obtain_access_token()

#twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

toronto = twitter.get_place_trends(id=2487956)
trend_array = []
if toronto:
   for trend in toronto[0].get('trends', []):
      trend_array.append(trend['name'])

#print trend_array
longstring = ''''''

search = trend_array[0]

var = raw_input("Enter the hashtag you would like to use: ")

if (var != ""):
   search = var

if (search[0] == '#'):
   search = search[1:]


print search 

avgTweetLength = 0

print "searching for tweets"
#goes through results and print out the actual tweet
results = twitter.search(q=search, count=500)

counter = 0

print "sorting the statuses"
for result in results['statuses']:
   longstring += result['text']
   avgTweetLength += len(result['text'])
   counter += 1

if (counter == 0):
   print "No tweets were found"
   exit()

print avgTweetLength
avgTweetLength = avgTweetLength / counter
print avgTweetLength                         
    
text_model = markovify.Text(longstring)

update = "None"

print "entering while loop"
while(counter != 0):
   update = text_model.make_short_sentence(avgTweetLength)
   counter -= 1
   print counter,
   if (update != "None"):
      print "not none"
      break

   
   
print update

#twitter.update_status(status=)

