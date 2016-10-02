#!/usr/bin/env python -W ignore

from twython import Twython
import markovify
import os

# Set these values
APP_KEY = os.environ['CONSUMER_KEY'] 
APP_SECRET = os.environ['CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['ACCESS_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']


#twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
#ACCESS_TOKEN = twitter.obtain_access_token()
#twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

#Global variables 
counter = 0
longstring = ''''''
avgTweetLength = 0
postLength = 140
user = False
maxid = 0

#Function used to read in tweets and adds them to a string used
#later to develop model
def createTweetString(results):
   global counter, longstring, avgTweetLength
   if (user):   
      for result in results:
         text = result['text']
         if "RT" in text:
            text = text.replace("RT", "", 1)
            
         
         if "https://t.c" in text:
            indexOfHTTPS = text.index("https://t.c")
            begIndex = indexOfHTTPS
            while(indexOfHTTPS < len(text) and (text[indexOfHTTPS] != ' ' or text[indexOfHTTPS] != '\n')):
                  indexOfHTTPS += 1
                  
            text = text[:begIndex] + text[indexOfHTTPS:]
            

         longstring += text
         avgTweetLength += len(result['text'])
         counter += 1
   else:
            
      for result in results['statuses']:
         text = result['text']
         if "RT" in text:
            text = text.replace("RT", "", 1)
            
         
         if "https://t.c" in text:
            indexOfHTTPS = text.index("https://t.c")
            begIndex = indexOfHTTPS
            while(indexOfHTTPS < len(text) and (text[indexOfHTTPS] != ' ' or text[indexOfHTTPS] != '\n')):
                  indexOfHTTPS += 1
                  
            text = text[:begIndex] + text[indexOfHTTPS:]
            

         longstring += text
         avgTweetLength += len(result['text'])
         counter += 1

   #Calculate the average tweet length
   postLength = avgTweetLength / counter
   
   if (counter == 0):
      print "No tweets were found"
      exit()

   
#Access twitter
twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def fetchTweets(search):
   global user
   if (user and maxid != 0):
      return twitter.get_user_timeline(screen_name=search[1:], count=200, max_id=maxid)
   elif (search[0] == '@'):
      print "it's a fucking user"
      user = True
      return twitter.get_user_timeline(screen_name=search[1:], count=200)
   elif(maxid != 0):
      return twitter.search(q=search, max_id=maxid)
   else:
      user = False
      #goes through results and print out the actual tweet
      return twitter.search(q=search, count=100)

   

#Get the place (right now default is SF)
#and get an array of trending hashtags from that
#location
toronto = twitter.get_place_trends(id=2487956)
trend_array = []
if toronto:
   for trend in toronto[0].get('trends', []):
      trend_array.append(trend['name'])

#Get the top trending hashtag
search = trend_array[0]

#Prompt the user to enter hashtag
print "The most popular hashtags are ", 
for i in range(0,10):
   print trend_array[i], 
   print ",",
var = raw_input("\nEnter the hashtag you would like to use: ")

#Search the user input hashtag is there is one - otherwise
#use the most popular
if (var != ""):
   search = var

if (search[0] == '#'):
   search = search[1:]


#Output search
print "Searching for hashtag ",
print search 


print "Fetching Tweets"
results = fetchTweets(search)
print "gon' create that long string"
#Create the string of all the fetched tweets
createTweetString(results)


#Variable to test if tweet has been generated
update = "None"
print "we gon b alright"
print type(longstring)
#Loop until tweet is generated
for i in range(0,15): 
   #Generate a markovift model of the string
   text_model = markovify.Text(longstring)

   #Attempt to generate a new tweet
   update = text_model.make_short_sentence(postLength)
   
   #If no tweet was generated then read in more tweets from twitter and try
   #again
   if (update == None):
      #add more tweets to the long string
      #results = twitter.search(q=search, max_id=results['statuses'][-1]['id_str'])
      maxid = results[-1]['id_str']
      results = fetchTweets(search)
      #Recreate the string of tweets
      
      createTweetString(results)
      print "Reading in more tweets"
      continue

   #Otherwise break out
   else:
      print "Created a Tweet:",
      print update
      print "Press enter to continue and tweet."
      if (raw_input("Would you like to try again? Type \"Yes\":") != ""):
         #add more tweets to the long string
         maxid = results['statuses'][-1]['id_str']
         results = fetchTweets(search)
         #Recreate the string of tweets
         createTweetString(results)
         print len(longstring)
         continue
      else:
         break

if(update == None):
   print "Unable to generate tweet -- try again"
   exit()

#Otherwise 
twitter.update_status(status=update)

