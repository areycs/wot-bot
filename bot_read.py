#!/usr/bin/python
import praw

reddit = praw.Reddit('WOTbot')

subreddit = reddit.subreddit("paranormal")

posts = []

for submission in subreddit.hot(limit=5):
  post = [submission.title, submission.selftext]

  posts.append(post)

  # print("Title: ", submission.title)
  # print("Text: ", submission.selftext)
  # print("Score: ", submission.score)
  # print("---------------------------------\n")

print(posts)
