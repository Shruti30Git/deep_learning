import streamlit as st
import requests
from PIL import Image
import os

# API details
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}  # Replace with your API token

# Function to query the API
def query(image_path):
    """Send the image to the Hugging Face API and retrieve the caption."""
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    response.raise_for_status()  # Raise an error for invalid responses
    return response.json()

# Streamlit app
def image_captioning_page():
    st.title("Image Captioning App")
    st.write("Upload an image, and the app will generate a caption.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Process the image when the button is clicked
        if st.button("Generate Caption"):
            with st.spinner("Processing..."):
                try:
                    # Save the uploaded image to a temporary file
                    temp_file = "temp_image.jpg"
                    with open(temp_file, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    # Call the API and get the output
                    output = query(temp_file)

                    # Clean up temporary file
                    os.remove(temp_file)

                    # Display the result
                    if "generated_text" in output[0]:
                        st.success("Generated Caption:")
                        st.write(output[0]["generated_text"])
                    else:
                        st.error("Failed to generate a caption. Please try again.")
                except requests.exceptions.RequestException as e:
                    st.error(f"API Error: {e}")
                except Exception as e:
                    st.error(f"Unexpected Error: {e}")
