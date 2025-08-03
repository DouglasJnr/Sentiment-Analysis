import streamlit as st
import numpy as np
import pickle
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.twitter_api import authenticate_twitter, fetch_tweets
from utils.preprocessing import clean_text
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils.twitter_api import check_rate_limit

rate_limit_info = check_rate_limit()
if rate_limit_info["remaining"] is not None:
    st.sidebar.write(f"**Rate Limit Remaining:** {rate_limit_info['remaining']}")
    from datetime import datetime
    reset_time = datetime.fromtimestamp(rate_limit_info["reset_timestamp"])
    st.sidebar.write(f"**Resets At:** {reset_time.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.sidebar.warning("Could not retrieve rate limit info.")

#load resources
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'sentiment_rnn.keras')
model = load_model(MODEL_PATH)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKENIZER_PATH = os.path.join(BASE_DIR, '..', 'models', 'tokenizer.pkl')
tokenizer = pickle.load(open(TOKENIZER_PATH, 'rb'))

st.title("Real-Time Twitter Sentiment Analysis")

query = st.text_input("Enter a Twitter search query (e.g 'Cryptocurrency', 'AI', 'elections')")

if st.button("Analyze"):
    client = authenticate_twitter()
    tweets = fetch_tweets(client, query)

    if not tweets:
        st.warning("No Tweets found")
    else:
        st.subheader("Live Sentiment Results")
        cleaned = [clean_text(tweet) for tweet in tweets]
        sequences = tokenizer.texts_to_sequences(cleaned)
        padded = pad_sequences(sequences, maxlen=100)

        predictions = model.predict(padded)
        sentiment_labels = ["Irrelevant", "Negative", "Neutral", "Positive" ]  # Adjust based on your model's classes
        predicted_classes = np.argmax(predictions, axis=1)
        sentiments = [sentiment_labels[i] for i in predicted_classes]

        for tweet, sentiment in zip(tweets, sentiments):
            st.markdown(f"**{sentiment}** : {tweet}")