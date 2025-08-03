import tweepy
from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Authenticate with Twitter API using Bearer Token
def authenticate_twitter():
    client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'), wait_on_rate_limit=True)
    return client

# Check rate limit from the Twitter API client
def check_rate_limit_from_client(client):
    response = client.search_recent_tweets(query="test", max_results=10, tweet_fields=["id"])
    headers = client.get_last_response().headers
    return {
        "remaining": int(headers.get("x-rate-limit-remaining")),
        "reset_timestamp": int(headers.get("x-rate-limit-reset"))
    }

# Fetch tweets based on a query
def fetch_tweets(client, query, max_tweets=15):
    tweets = client.search_recent_tweets(query=query, max_results=max_tweets, tweet_fields=["text"])
    return [tweet.text for tweet in tweets.data] if tweets.data else []