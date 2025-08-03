import tweepy
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def authenticate_twitter():
    client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'), wait_on_rate_limit=True)
    return client


HEADERS = {"Authorization": f"Bearer {os.getenv('TWITTER_BEARER_TOKEN')}"}


def check_rate_limit():
    url = "https://api.twitter.com/2/tweets/search/recent"
    response = requests.get(url, headers=HEADERS, params={"query": "test", "max_results": 10})

    remaining = response.headers.get("x-rate-limit-remaining")
    reset = response.headers.get("x-rate-limit-reset")

    return {
        "remaining": int(remaining) if remaining else None,
        "reset_timestamp": int(reset) if reset else None
    }


def fetch_tweets(client, query, max_tweets=15):
    tweets = client.search_recent_tweets(query=query, max_results=max_tweets, tweet_fields=["text"])
    return [tweet.text for tweet in tweets.data] if tweets.data else []