from urlToApiIP import converter
from jsonAdditionalResponse import extraTweets
from tweetCleaner import cleaner

from bs4 import BeautifulSoup
import requests
import sys
import time

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
tweetReplyContent = []

def replyRet(url):
	time.sleep(20)
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "lxml")
	tweetReplyList = soup.find(class_='stream')
	if tweetReplyList is not None:
		tweetReply = tweetReplyList.find_all('p')
		tweetReplyList = soup.findAll(attrs = {'class' : 'tweet-timestamp js-permalink js-nav js-tooltip'})
		for content in tweetReply:
			if content is not None:
				content = content.prettify().translate(non_bmp_map)
				tweetReplyContent.append(content)
		user, tweetId = converter(url)
		extraTweetReplyList, extraTweetReplyContent = extraTweets(user, tweetId)
		if extraTweetReplyList is not None:
			for i in extraTweetReplyList:
				tweetReplyList.append(i)
			for i in extraTweetReplyContent:
				tweetReplyContent.append(i)
		for i in range(len(tweetReplyContent)):
			tweetReplyContent[i] = cleaner(tweetReplyContent[i])
		return tweetReplyList, tweetReplyContent
	else:
		return None, None

if __name__ == "__main__":
    #for testing whether it returns the values properly!
    tweetReplyListItems, tweetReplyContentItems = replyRet("https://twitter.com/olympicchannel/status/1001508970962571265")
    for i in range(1,len(tweetReplyListItems)):
        print("Reply " + (str)(i) + ": ")
        print("https://www.twitter.com" + tweetReplyListItems[i]['href']) #Reply links
        print(tweetReplyListItems[i]['title']) #Date and time of replies
        print(tweetReplyContentItems[i-1]) #Actual replies
