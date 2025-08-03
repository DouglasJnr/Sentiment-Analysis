import tweepy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Authenticate with Twitter API using Bearer Token
def authenticate_twitter():
    client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'), wait_on_rate_limit=True)
    return client

# Fetch tweets based on a query
def fetch_tweets(client, query, max_tweets=10):
    try:
        tweets = client.search_recent_tweets(query=query, max_results=max_tweets, tweet_fields=["text"])
        return [tweet.text for tweet in tweets.data] if tweets.data else []

    except tweepy.errors.Forbidden:
        return [], "monthly_cap"

    except tweepy.errors.TooManyRequests:
        return [], "rate_limit"

    except Exception:
        return [], "error"