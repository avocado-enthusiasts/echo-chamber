#!/usr/bin/python3

import praw, json, requests, io, os, pathlib, pprint
from collections import defaultdict

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
  count = 0
  with open('subreddit_list_10.txt') as subreddit_list:
    for line in subreddit_list:
      subreddit_name = line.strip()
      subreddit = r.subreddit(subreddit_name)
      home_dir = str(pathlib.Path.home())
      subreddit_dir = home_dir + '/reddit/' + subreddit_name
      os.makedirs(subreddit_dir, exist_ok = True)
      print(subreddit_name)
      for submission in subreddit.hot(limit=1000):
        submission_id = submission.id
        print(submission_id)
        submission_file = subreddit_dir + '/' + submission_id
        with open(submission_file, 'w') as sub_file:
          req_path = 'https://api.pushshift.io/reddit/submission/comment_ids/' + submission_id
          req = requests.get(req_path)
          ids = req.json()
          for cid in ids['data']:
            body = r.comment(cid).body
            if body and body != '[deleted]' and body != '[removed]':
              sub_file.write(body + '/n')
        

      # print(subreddit.display_name)
      # pprint.pprint(vars(subreddit))

      # print(subreddit.display_name)
      # print(subreddit.subscribers)


  # req = requests.get('https://api.pushshift.io/reddit/submission/comment_ids/9xwtzs')
  # ids = req.json()
  # start = timer()
  # count = 0
  # for cid in ids['data']:
  #   body = r.comment(cid).body
  #   if body and body != '[deleted]' and body != '[removed]':
  #     print(body+'\n')
  # end = timer()
  # total = end - start
  # subreddit_name = 'EnoughTrumpSpam'
  # item_map = defaultdict(list)
  # submissions = []
  # count = 10


  # get_ids(r, subreddit_name, count, submissions)
  # process_submissions(item_map, submissions)

  # print(item_map)

if __name__ == '__main__':
  main()