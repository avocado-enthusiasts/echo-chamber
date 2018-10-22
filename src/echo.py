import praw
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
  subreddit_name = 'EnoughTrumpSpam'
  item_map = defaultdict(list)
  submissions = []
  count = 10

  if r.read_only:
    print('Not authorized!')
    raise NotImplementedError

  get_ids(r, subreddit_name, count, submissions)
  process_submissions(item_map, submissions)

  print(item_map)

if __name__ == '__main__':
  main()