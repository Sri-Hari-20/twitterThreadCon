def cleaner(tweet):
    buffer = ""
    flag = 0
    for i in tweet:
        if i == "<":
            flag = 1
        elif i == ">":
            flag = 0
        elif flag == 0:
            if i != '\n' and i != '\t':
                buffer = buffer + i
    return buffer

if __name__ == "__main__":
    sampleTweet = r"""<p class="TweetTextSize js-tweet-text tweet-text" data-aria-label-part="0" lang="en">
 <a class="twitter-timeline-link" data-expanded-url="http://nokriadda.in" dir="ltr" href="https://t.co/b99wSlp8LU" rel="nofollow noopener" target="_blank" title="http://nokriadda.in">
  <span class="tco-ellipsis">
  </span>
  <span class="invisible">
   http://
  </span>
  <span class="js-display-url">
   nokriadda.in
  </span>
  <span class="invisible">
  </span>
  <span class="tco-ellipsis">
   <span class="invisible">
   </span>
  </span>
 </a>
 a latest govt jobs portal information
</p>"""
    print(cleaner(sampleTweet))