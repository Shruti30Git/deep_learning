import streamlit as st
import requests
from PIL import Image
import io

# API details
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query_text_to_image(prompt):
    """Query the Hugging Face API to generate an image from text."""
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    # Raise an exception for bad requests
    response.raise_for_status()

    # Return the binary image content
    return response.content


def text_to_image_page():
    """Text-to-Image Generation Page."""
    st.title("Text-to-Image Generator")
    st.write("Enter a text prompt to generate an image using the FLUX model.")

    # Input field for the text prompt
    prompt = st.text_input("Enter your text prompt:")

    # Generate image when the button is clicked
    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            try:
                # Query the API
                image_content = query_text_to_image(prompt)

                # Load the image from the binary content
                image = Image.open(io.BytesIO(image_content))

                # Convert the image to a downloadable format
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                buf.seek(0)

                # Display the generated image
                st.image(image, caption=f"Generated Image for: {prompt}", use_column_width=True)

                # Add download button
                st.download_button(
                    label="Download Image",
                    data=buf,
                    file_name="generated_image.png",
                    mime="image/png"
                )
            except requests.exceptions.RequestException as e:
                st.error(f"Error querying the API: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

