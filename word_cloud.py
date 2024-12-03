import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO

# Function to generate word cloud and provide download option
def wordcloud_page():
    # Title of the app
    st.title("Word Cloud Generator")

    # Sidebar with instructions
    st.sidebar.title("Instructions")
    st.sidebar.image(
        "https://i.postimg.cc/fybkVcyq/images.png",
        use_column_width=True)
    st.sidebar.write("""
    1. Enter a few lines of text or a prompt in the text box.
    2. Click 'Generate Word Cloud' to visualize the most frequent words.
    3. The word cloud will update based on the text you provide.
    """)

    # Input field for user to enter text or prompt
    user_input = st.text_area("Enter your text or prompt here:")

    # Function to generate word cloud
    def generate_wordcloud(text):
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        return wordcloud

    # Generate word cloud when the user clicks the button
    if st.button("Generate Word Cloud"):
        if user_input:
            # Generate and display the word cloud
            wordcloud = generate_wordcloud(user_input)

            # Display the word cloud using matplotlib
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')  # Hide axes
            st.pyplot(plt)  # Show the plot in Streamlit

            # Create a BytesIO object to save the image for download
            image_buffer = BytesIO()
            wordcloud.to_image().save(image_buffer, format='PNG')
            image_buffer.seek(0)

            # Add a download button
            st.download_button(
                label="Download Word Cloud Image",
                data=image_buffer,
                file_name="wordcloud.png",
                mime="image/png"
            )
        else:
            st.warning("Please enter some text to generate the word cloud.")
