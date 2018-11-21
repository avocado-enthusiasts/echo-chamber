#!/usr/bin/python3

import praw, json, requests
from collections import defaultdict
from timeit import default_timer as timer

def get_items(comment, item_list):
  item_list.append(comment)
  if not hasattr(comment, 'replies'):
    replies = comment.comments()
  else:
    replies = comment.replies
  for child in replies:
    get_items(child, item_list)

def get_ids(r, subreddit_name, count, submissions):
  subreddit = r.subreddit(subreddit_name)
  for submission in subreddit.hot(limit=count):
    submissions.append(submission)

def process_submissions(item_map, submissions):
  for submission in submissions:
    print('Processing submission', submission.id)
    for comment in submission.comments:
      get_items(comment, item_map[submission.id])



def main():
  r = praw.Reddit(user_agent='Python:echo-chamber:v0.0.1')
  if r.read_only:
    print('Not authorized!')
    return

  req = requests.get('https://api.pushshift.io/reddit/submission/comment_ids/9xwtzs')
  ids = req.json()
  start = timer()
  count = 0
  for cid in ids['data']:
    body = r.comment(cid).body
    if body != '[deleted]' and body != '[removed]':
      count += 1
      print(body+'\n')
  end = timer()
  total = end - start
  # subreddit_name = 'EnoughTrumpSpam'
  # item_map = defaultdict(list)
  # submissions = []
  # count = 10


  # get_ids(r, subreddit_name, count, submissions)
  # process_submissions(item_map, submissions)

  # print(item_map)

if __name__ == '__main__':
  main()