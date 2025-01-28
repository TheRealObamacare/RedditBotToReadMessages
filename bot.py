import praw

def connect_to_reddit():
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='MyRedditBot/1.0'
    )
    return reddit

if __name__ == "__main__":
    reddit_instance = connect_to_reddit()
    # Example usage:
    subreddit = reddit_instance.subreddit("python")
    for submission in subreddit.hot(limit=3):
        print(submission.title)