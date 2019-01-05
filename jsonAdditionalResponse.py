import urllib.request
import json
from six.moves import urllib
from bs4 import BeautifulSoup
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

jsonRequestFormat = ['?include_available_features=1&include_entities=1&max_position=DAACDwABCgAAAA4Od-qcNJVgAA536Jc91sABDnfq40AWsAAOd_njRxbAAA536Djel-AFDnfw_3hU0AAOd_nNBlfgAA538ibBl7ABDnfoHGxXcAAOeAGD1ZewAQ539CpKFOABDnfrvuXXsAAOeAjQzdeAAA54CHI3FeABCAADAAAAAQIABAAAAA&reset_error_state=false','?include_available_features=1&include_entities=1&max_position=DAACDwABCgAAACAOd-qcNJVgAA536Jc91sABDnf540cWwAAOd-rjQBawAA536Djel-AFDnfw_3hU0AAOd_ImwZewAQ54AYPVl7ABDnf5zQZX4AAOd_QqShTgAQ537PsdF7AADnfoHGxXcAAOeAy46FRwAA54BYplFrAADngDB6dWsAEOd-u-5dewAA54GHvtV4ABDngVDA5XsAAOeBKP25fgAQ54EbUTFsABDngQdNYX4AMOeA9RkdfQAA54Dzm7FrACDngOvsVX4AAOeA6bLhbAAQ54DQWaFuABDngMaTwXsAEOeAuiIhXgAA54CYo-VeACDngJZBZWwAEOeAjwmteAAA54CNDN14AACAADAAAAAQIABAAAAA&reset_error_state=false']
tweetContent = []
tweetLink = []

def extraTweets(user, TweetID):
	for i in jsonRequestFormat:
		url = 'https://twitter.com/i/'+user+'/conversation/'+(str)(TweetID)+i
		response = urllib.request.urlopen(url)
		data = json.load(response)
		soup = BeautifulSoup((data['items_html']),"html.parser")
		tweetHTML = soup.findAll('p')
		tweetInfo = soup.findAll(attrs = {'class' : 'tweet-timestamp js-permalink js-nav js-tooltip'})
		for tweet in tweetHTML:
			if tweet is not None:
				tweet = (tweet.prettify().translate(non_bmp_map))
				tweetContent.append(tweet)
		for link in tweetInfo:
			tweetLink.append(link)
	return tweetLink, tweetContent

if __name__ == '__main__':
	tweetLink, tweets = extraTweets("olympicchannel","1001508970962571265")
	print(len(tweetContent))