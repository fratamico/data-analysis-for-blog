import twitter
#maybe collect every hour from 

CONSUMER_KEY = 'Czjs45IabmVBz4ZmleWGoxOaX'
CONSUMER_SECRET ='mHRmNbzjwo57mYVRmk8crDT4CjWZ8DO9CipmPSsVAT3S5gyPP1'
OAUTH_TOKEN = '414528346-TcrNkPcYDJkFmOkmSXHp93J2cpe89LTN7xdM5Go9'
OAUTH_TOKEN_SECRET = 'CiylvodoMo4jmmFo93LQSXhsqKW9r1xwJj2uWiWqH8ekG'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)


q = ''
geocode_SF = '37.759193,-122.444810,4mi' 
until = '2015-02-24'

count = 100

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, geocode=geocode, count=count)
print search_results
print len(search_results["statuses"])
for query in search_results["statuses"]:
    print query["text"]
    print query["created_at"]




geocode_van = '49.257876, -123.169003,4mi'

geocode_SD = '32.779369,-117.252733,9mi' #chose point near mission beach so i could include downtown, point loma, la jolla, and the biotech industry area. note that this is a lot of space on the coast







