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


counter = 0
longstring = ''''''
avgTweetLength = 0


def createTweetString(results):
   global counter, longstring, avgTweetLength
   for result in results['statuses']:
      longstring += result['text']
      avgTweetLength += len(result['text'])
      counter += 1
   if (counter == 0):
      print "No tweets were found"
      exit()

   

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

toronto = twitter.get_place_trends(id=2487956)
trend_array = []
if toronto:
   for trend in toronto[0].get('trends', []):
      trend_array.append(trend['name'])

#print trend_array

search = trend_array[0]

var = raw_input("Enter the hashtag you would like to use: ")

if (var != ""):
   search = var

if (search[0] == '#'):
   search = search[1:]


print search 


print "searching for tweets"
#goes through results and print out the actual tweet
results = twitter.search(q=search, count=100)

createTweetString(results)

print avgTweetLength
postLength = avgTweetLength / counter
print postLength 

update = "None"

print "entering while loop"
while(counter != 0):
   text_model = markovify.Text(longstring)
   update = text_model.make_short_sentence(postLength)
   counter -= 1
   print counter,
   if (update == None):
      print postLength
      #raw_input("Press Enter to continue")
      #add more tweets to the long string
      results = twitter.search(q=search, max_id=results['statuses'][-1]['id_str'])
      
      createTweetString(results)
      print "got none"
      continue
   else:
      print "breaking"
      break

   
   
print update

#twitter.update_status(status=)

