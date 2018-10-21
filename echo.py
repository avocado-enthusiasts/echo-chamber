import praw

reddit = praw.Reddit(user_agent='linux:echo-chamber:v0.0.1')

print(reddit.read_only)
for submission in reddit.subreddit('learnpython').hot(limit=10):
  print(submission.title)