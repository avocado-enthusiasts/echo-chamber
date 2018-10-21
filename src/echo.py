import praw

reddit = praw.Reddit(user_agent='Python:echo-chamber:v0.0.1')

print('Authorized:',str(not reddit.read_only))

subreddit = reddit.subreddit('EnoughTrumpSpam')

for submission in subreddit.hot(limit=10):
    print(submission.title)  # Output: the submission's title
    print(submission.score)  # Output: the submission's score
    print(submission.id)     # Output: the submission's ID
    print(submission.url)    # Output: the URL the submission points to
                             # or the submission's URL if it's a self post