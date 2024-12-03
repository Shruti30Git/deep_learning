# urltotext.py

import streamlit as st
from huggingface_hub import InferenceClient

# Initialize Hugging Face InferenceClient
client = InferenceClient(api_key="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")

# Function to generate image description using Hugging Face model
def describe_image(url):

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image in one sentence."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url
                    }
                }
            ]
        }
    ]

    # Requesting description from Hugging Face model
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.2-11B-Vision-Instruct",
        messages=messages,
        max_tokens=500
    )
    return completion.choices[0].message["content"]

def urltotext_page():
    # Title for the app
    st.title("Image Description Generator")
    st.sidebar.title("Instructions")
    st.sidebar.write("""
            1. Enter a URL.
            2. It will generate text

            """)
    # Input for image URL
    image_url = st.text_input("Enter the URL of the image you want described:")

    # When the user inputs a URL
    if image_url:
        with st.spinner("Generating description..."):
            try:
                # Get the description from the model
                description = describe_image(image_url)
                st.success("Description generated successfully!")
                st.image(image_url, caption="Uploaded Image")
                st.write("**Generated Description:**", description)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.info("Please enter an image URL above to get started.")
