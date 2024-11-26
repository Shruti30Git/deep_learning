import streamlit as st
import requests
from pathlib import Path
import json

# API details
API_URL = "https://api-inference.huggingface.co/models/google/vit-base-patch16-224"
headers = {"Authorization": "Bearer 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"}  # Replace with your token

# Function to query the Hugging Face ViT model
def query(image_path):
    """Send the image file to the Hugging Face API and get the response."""
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    try:
        response.raise_for_status()
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def format_results(output):
    """Format the results to show only labels and accuracy scores."""
    results = []
    if isinstance(output, list):  # Check if the output is a list of classifications
        for item in output:
            label = item.get("label", "Unknown")
            score = round(item.get("score", 0) * 100, 2)
            results.append(f"{label}: {score}%")
    return results

def image_classification_page():
    """Image Classification Page."""
    st.title("Image Classification with Hugging Face ViT")
    st.markdown("Upload an image to classify its content using the ViT model!")

    # Image upload
    uploaded_file = st.file_uploader("Upload an Image (PNG/JPG/JPEG)", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        # Save the uploaded image temporarily
        save_folder = Path("uploaded_images")
        save_folder.mkdir(parents=True, exist_ok=True)
        save_path = save_folder / uploaded_file.name
        with open(save_path, mode="wb") as f:
            f.write(uploaded_file.getvalue())

        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Submit button
        if st.button("Classify Image"):
            try:
                # Query the Hugging Face API
                output = query(str(save_path))

                # Check for errors in the response
                if "error" in output:
                    st.error(f"API Error: {output['error']}")
                else:
                    # Display classification results
                    st.markdown("**Classification Results (Labels and Accuracy Scores):**")
                    results = format_results(output)
                    for result in results:
                        st.write(result)



            except Exception as e:
                st.error(f"Error while querying the API: {e}")


