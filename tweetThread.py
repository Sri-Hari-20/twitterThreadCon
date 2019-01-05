from bs4 import BeautifulSoup
from jsonAdditionalResponse import extraTweets
import csv
import requests
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


tweetReplyContent = []

def replyRet(user, tweetId):
	url = "https://www.twitter.com/"+user+"/status/"+tweetId
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "lxml")
	tweetReplyList = soup.find(class_='stream')
	tweetReply = tweetReplyList.find_all('p')
	tweetReplyList = soup.findAll(attrs = {'class' : 'tweet-timestamp js-permalink js-nav js-tooltip'})
	for content in tweetReply:
		if content is not None:
			content = content.prettify().translate(non_bmp_map)
			tweetReplyContent.append(content)
	extraTweetReplyList, extraTweetReplyContent = extraTweets(user, tweetId)
	for i in extraTweetReplyList:
		tweetReplyList.append(i)
	for i in extraTweetReplyContent:
		tweetReplyContent.append(i)
	#Clean tweetReplyContent here
	return tweetReplyList, tweetReplyContent

if __name__ == "__main__":
    #for testing whether it returns the values properly!
    tweetReplyListItems, tweetReplyContentItems = replyRet("olympicchannel","1001508970962571265")
    for i in range(1,len(tweetReplyListItems)):
        print("Reply " + (str)(i) + ": ")
        print(tweetReplyListItems[i]['href'])
        print(tweetReplyListItems[i]['title'])
        print(tweetReplyContentItems[i-1])