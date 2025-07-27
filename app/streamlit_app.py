import streamlit as st
from utils.twitter_api import authenticate_twitter, fetch_tweets
from utils.preproceessing import clean_text
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

#load resources
model = load_model('models/sentiment_rnn.h5')
tokenizer = pickle.load(open('models/tokenizer.pkl', 'rb'))

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
        sentiments = ["Positive" if p > 0.5 else "Negative" for p in predictions]

        for tweet, sentiment in zip(tweets, sentiments):
            st.markdown(f"**{sentiment}** : {tweet}")