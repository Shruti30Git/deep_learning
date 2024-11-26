import requests
import streamlit as st
from pathlib import Path

# API details
API_URL = "https://api-inference.huggingface.co/models/facebook/detr-resnet-50"
headers = {"Authorization": "Bearer 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"}  # Replace 'your_token' with your actual token

def query(filename):
    """Send the image file to the Hugging Face API and get the response."""
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def save_uploaded_file(uploaded_file, save_folder="C:/FDP"):
    """Save the uploaded file to the specified folder."""
    save_folder = Path(save_folder)
    save_folder.mkdir(parents=True, exist_ok=True)

    # Save the file
    save_path = save_folder / uploaded_file.name
    with open(save_path, mode="wb") as w:
        w.write(uploaded_file.getvalue())

    return save_path

def filter_objects_by_score(objects, threshold=0.50):
    """Filter out objects with a score below the threshold."""
    return [
        obj for obj in objects if obj['score'] >= threshold
    ]

def object_detection_page():
    """Object detection page for the Streamlit app."""
    st.title("Object Detection")
    st.markdown("**Please Upload the file:**")

    uploaded_file = st.file_uploader(label="Upload file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        with st.form(key="Upload Form", clear_on_submit=True):
            submit = st.form_submit_button(label="Submit")

        if submit:
            try:
                # Save the uploaded file
                save_path = save_uploaded_file(uploaded_file)

                if save_path.exists():
                    st.success(f"File '{uploaded_file.name}' is successfully saved!")

                # Send the saved file to the Hugging Face API for object detection
                output = query(str(save_path))

                # Filter objects based on score
                filtered_output = filter_objects_by_score(output, threshold=0.7)

                # Display filtered results
                if filtered_output:
                    st.markdown("**Filtered Objects (with score >= 0.5):**")
                    for obj in filtered_output:
                        st.write(f"Object : {obj['label']}, Score : {obj['score']}")
                        #st.write(f"Bounding Box: {obj['box']}")

                else:
                    st.write("No objects with score >= 0.7 found.")

            except Exception as e:
                st.error(f"Error while processing the file: {e}")
