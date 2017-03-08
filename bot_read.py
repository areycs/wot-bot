#!/usr/bin/python
import praw

reddit = praw.Reddit('WOTbot')

subreddit = reddit.subreddit("paranormal")

posts = []

for submission in subreddit.hot(limit=5):
  
  postText   = submission.selftext
  charLength = len(submission.selftext)
  lineBreaks = submission.selftext.count("\n")
  
  if charLength == 0:
  	if lineBreaks == 0:
  		charBreakRatio = "N/A"
  	
  else:
  	charBreakRatio = charLength / lineBreaks

  print("Text: ", postText)
  print("Char Length: ", charLength)
  print("Line Breaks: ", lineBreaks)
  print("Char to Break Ratio: ", str(charBreakRatio) + ":1")
  # print("Score: ", submission.score)
  print("---------------------------------\n")

