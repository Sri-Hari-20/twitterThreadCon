from urlToApiIP import converter
from tweetCleaner import cleaner

from bs4 import BeautifulSoup
import sys
import time
from selenium import webdriver

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
tweetReplyContent = []

def replyRet(url):
	driver = webdriver.Firefox()
	driver.get(url)
	driver.execute_script("window.scrollTo(0, 250)")
	soup = BeautifulSoup(driver.page_source, "lxml")
	tweetReplyList = soup.find(class_='stream')
	if tweetReplyList is not None:
		tweetReply = soup.findAll(attrs = {'class' : 'TweetTextSize js-tweet-text tweet-text'})
		tweetReplyList = soup.findAll(attrs = {'class' : 'tweet-timestamp js-permalink js-nav js-tooltip'})
		for content in tweetReply:
			if content is not None:
				content = content.prettify().translate(non_bmp_map)
				tweetReplyContent.append(content)
		user, tweetId = converter(url)
		for i in range(len(tweetReplyContent)):
			tweetReplyContent[i] = cleaner(tweetReplyContent[i])
		driver.quit()
		return tweetReplyList, tweetReplyContent
	else:
		driver.quit()
		return None, None

if __name__ == "__main__":
    #for testing whether it returns the values properly!
    tweetReplyListItems, tweetReplyContentItems = replyRet("https://twitter.com/olympicchannel/status/1001508970962571265")
    for i in range(1,len(tweetReplyListItems)):
        print("Reply " + (str)(i) + ": ")
        print("https://www.twitter.com" + tweetReplyListItems[i]['href']) #Reply links
        print(tweetReplyListItems[i]['title']) #Date and time of replies
        print(tweetReplyContentItems[i-1]) #Actual replies
