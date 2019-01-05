import urllib.request
import requests
import json
import csv
from six.moves import urllib
from bs4 import BeautifulSoup

# url = "https://twitter.com/i/olympicchannel/conversation/1001508970962571265/?include_available_features=1&include_entities=1&max_position=DAACDwABCgAAAA4Od-qcNJVgAA536Jc91sABDnfq40AWsAAOd_njRxbAAA536Djel-AFDnfw_3hU0AAOd_nNBlfgAA538ibBl7ABDnfoHGxXcAAOeAGD1ZewAQ539CpKFOABDnfrvuXXsAAOeAjQzdeAAA54CHI3FeABCAADAAAAAQIABAAAAA&reset_error_state=false"
# response = urllib.request.urlopen(url)
# data = json.load(response)
response = requests.get("https://twitter.com/olympicchannel/status/1001508970962571265")
soup = BeautifulSoup(response.content,"html.parser")
tweetList = soup.findAll('p')
tweetInfo = soup.findAll(attrs = {'class' : 'tweet-timestamp js-permalink js-nav js-tooltip'})
mentionsInfo = soup.findAll(attrs = {'class' : 'twitter-atreply pretty-link js-nav'})

for mention in mentionsInfo:
	print(mention['href'])

#Get the mentions from a tweet
for i in range(len(tweetList)):
	print("Reply " + str(i))
	mentions = tweetList[i].findAll(attrs = {'class' : 'twitter-atreply pretty-link js-nav'})
	for mention in mentions:
		print(mention['href'])