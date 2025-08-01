import tweepy
from dotenv import load_dotenv
import os

def authenticate_twitter():
    load_dotenv()
    client = tweepy.Client(bearer_token=os.getenv('TWITTER_BEARER_TOKEN'), wait_on_rate_limit=True)
    return client

def fetch_tweets(client, query, max_tweets=15):
    tweets = client.search_recent_tweets(query=query, max_results=max_tweets, tweet_fields=["text"])
    return [tweet.text for tweet in tweets.data] if tweets.data else []