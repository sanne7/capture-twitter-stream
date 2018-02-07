#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Import Json
import json

#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        try:
          j = json.loads(data)        
          print (j["text"])
          with open('tweets.data','a') as f:
           f.write(data)
          return True
        except KeyError:
          print ""


    def on_error(self, status):
       print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: '@SuperBowl', 'Patriots', 'Eagles'
    stream.filter(track=['@SuperBowl', 'Patriots', 'Eagles'])
