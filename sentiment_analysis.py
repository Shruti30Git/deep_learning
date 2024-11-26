import streamlit as st
import requests

def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/lxyuan/distilbert-base-multilingual-cased-sentiments-student"
    headers = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face API token
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Page function for Sentiment Analysis
def sentiment_analysis_page():
    st.title("Multilingual Sentiment Analysis")

    # Create text input box for user input
    text_input = st.text_area("Enter text for sentiment analysis:")

    # Create a button for triggering analysis
    if st.button("Analyze"):
        if text_input:
            # Query the Hugging Face API with the user input
            output = query({"inputs": text_input})

            # Check for the correct API response format
            if isinstance(output, list) and len(output) > 0 and isinstance(output[0], list):
                sentiment_data = output[0]  # This is the inner list containing sentiment info
                sentiment = sentiment_data[0].get('label', 'No sentiment label found')
                score = sentiment_data[0].get('score', 'No sentiment score found')

                # Display sentiment and score
                st.write(f"Sentiment: **{sentiment}**")
                st.write(f"Score: **{score:.4f}**")
            else:
                st.error("Error: Unexpected API response format.")
        else:
            st.error("Please enter some text for sentiment analysis.")

