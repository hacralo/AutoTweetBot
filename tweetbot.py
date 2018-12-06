import tweepy
import time

# credentials to login to twitter api, to get the api keys apply for developer account at apps.twitter.com, get approved takes at least 24 hours, then 
# create a new app under dev.twitter.com to generate api keys

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# api.update_status("test bot reply!")
# checking if all is fine, prints your username.
user = api.me()
print (user.name)

# search for text "halloween"
searchTerm = "halloween"  # search term
phrase = "hi, happy Halloween!" # any reply

for tweet in api.search(q=searchTerm,rpp=2):
	#rpp is number of tweets to return as list and there are other parameters refer documentation
	try:
		tweetId = tweet.user.id
		username = tweet.user.screen_name
		print(tweetId)
		print(username)
		api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
		print ("Replied with " + phrase)
		time.sleep(60) # tweets 1 tweet every 60 sec to avoid unnecessary spamming violations
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

# Alternate method:

# numberOfTweets = 2 # total number of tweets to reply, select any amount, limit it to 100 every 15 min, account may get banned for spamming
# for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
# 	try:
# 		tweetId = tweet.user.id
# 		username = tweet.user.screen_name
# 		print(tweetId)
# 		print(username)
# 		api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
# 		print ("Replied with " + phrase)
		
# 	except tweepy.TweepError as e:
# 	    print(e.reason)
# 	except StopIteration:
# 	    break