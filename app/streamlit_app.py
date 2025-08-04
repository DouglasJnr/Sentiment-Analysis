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

# Load the pre-trained model and tokenizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'sentiment_rnn.keras')
model = load_model(MODEL_PATH)

# Load the tokenizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKENIZER_PATH = os.path.join(BASE_DIR, '..', 'models', 'tokenizer.pkl')
tokenizer = pickle.load(open(TOKENIZER_PATH, 'rb'))

# --- Sidebar: Help Info ---
st.sidebar.title("📘 How to Use This App")
st.sidebar.markdown("""
1. Enter a topic or keyword (e.g., **AI**, **elections**, **Ethereum**).
2. Click **Analyze** to fetch recent tweets.
3. View real-time sentiment predictions below.
---
🔄 **Note:** Results are based on live Twitter data. If you see an error, you may have hit the monthly tweet limit.
""")

# --- Main Page Title ---
st.markdown("<h1 style='text-align: center; color: white;'>Real-Time Twitter Sentiment Analysis</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Analyze public sentiment on any topic using live tweets and an RNN model.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Main Content ---
# Input for Twitter search query
query = st.text_input("Enter a Twitter search query (e.g 'Cryptocurrency', 'AI', 'elections')")

# Button to trigger analysis
if st.button("Analyze"):
    client = authenticate_twitter()
    if not client:
        st.error("Failed to authenticate with Twitter API. Please check your credentials.")
        st.stop()

    # Fetch tweets based on the query
    tweets, error_type = fetch_tweets(client, query)

    # Display the number of tweets fetched
    if error_type == "monthly_cap":
        st.error("You may have exceeded your monthly tweet cap (10,000 tweets/month).")
    elif error_type == "error":
        st.error("An unexpected error occurred.")
    elif not tweets:
        st.warning("No Tweets found.")
    else:
    # Proceed with sentiment analysis...
        st.subheader("Live Sentiment Results")
        cleaned = [clean_text(tweet) for tweet in tweets]
        sequences = tokenizer.texts_to_sequences(cleaned)
        padded = pad_sequences(sequences, maxlen=100)

        predictions = model.predict(padded)
        sentiment_labels = ["Irrelevant", "Negative", "Neutral", "Positive" ]  # Adjust based on your model's classes
        predicted_classes = np.argmax(predictions, axis=1)
        sentiments = [sentiment_labels[i] for i in predicted_classes]

        for tweet, sentiment in zip(tweets, sentiments):
            st.markdown(f"<div style='margin-bottom: 15px;'><strong>{sentiment}:</strong> {tweet}</div>",
                        unsafe_allow_html=True)
