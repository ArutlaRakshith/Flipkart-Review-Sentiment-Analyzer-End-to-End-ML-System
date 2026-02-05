import streamlit as st
import requests

st.set_page_config(page_title="Flipkart Sentiment Analyzer", layout="centered")

st.title("Flipkart Product Review Sentiment Analyzer")
st.write("Enter a product review to analyze sentiment.")

API_URL = "http://13.60.136.48:8000/predict"

review_text = st.text_area("Review Text", placeholder="Type your review here...")

if st.button("Analyze Sentiment"):
    if not review_text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Analyzing... Please wait!"):
            response = requests.post(API_URL, json={"text": review_text})
            if response.status_code == 200:
                result = response.json()
                sentiment = result["sentiment"]
                confidence = result["confidence"]

                if sentiment == "positive":
                    st.success(f"Sentiment: {sentiment.upper()}")
                else:
                    st.error(f"Sentiment: {sentiment.upper()}")

                st.info(f"Confidence Level: {confidence}")
            else:
                st.error("Error connecting to API. Is FastAPI running?")


