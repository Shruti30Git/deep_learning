import streamlit as st
import requests

# API URL and headers
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"
headers = {"Authorization": "Bearer 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"}

# Function to query the Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit UI for Text Generation with Llama model
def llama_text_generation_page():
    st.title("Text Generation")

    #st.markdown("""This app uses the **Llama-3.2-1B** model from Hugging Face to generate text based on the provided input prompt.""")

    # User input for the prompt
    prompt = st.text_input("Enter the text prompt")

    # Generate prediction when button is clicked
    if st.button("Generate Text"):
        if prompt:
            try:
                # Send the input prompt to the model
                output = query({"inputs": prompt})

                # Display the result
                if output and 'generated_text' in output[0]:
                    generated_text = output[0]['generated_text']
                    st.markdown(f"**Generated Text:** {generated_text}")
                else:
                    st.error("No output received from the model.")
            except Exception as e:
                st.error(f"Error occurred: {e}")
        else:
            st.error("Please enter a valid prompt.")
