# main.py

import streamlit as st
from streamlit_option_menu import option_menu
from imagecaptioning import image_captioning_page
from imageclassification import image_classification_page
from texttoimage import text_to_image_page
from final_QR_Resume import qr_code_generator_page, resume_generator_page
from objdetetction import object_detection_page
from sentiment_analysis import sentiment_analysis_page
from textgeneration import llama_text_generation_page
from AIchatbot import chatbot_page
from word_cloud import wordcloud_page  # Import wordcloud page
from urltotext import urltotext_page  # Import urltotext page

# Main application
def main():
    # Custom CSS to increase font size and styling
    st.markdown("""
    <style>
        .css-1n3v2i4 {
            font-size: 20px !important;  /* Increase radio button font size */
        }
        .css-1v0mbdj {
            font-size: 18px !important;  /* Increase label font size */
        }
        .title {
            font-size: 32px !important;  /* Increase title font size */
            font-weight: bold;
        }
        .subsection-title {
            font-size: 28px !important;  /* Subsection heading size */
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create navigation bar with main sections and subsections
    selected_main = option_menu(
        menu_title=None,  # Title for navigation bar
        options=["Home", "AI Tools", "About", "Contact"],  # Main sections
        icons=["house", "tools", "info-circle", "envelope"],  # Icons for sections
        menu_icon="cast",  # Icon for the menu
        default_index=0,  # Default selected menu item
        orientation="horizontal",  # Horizontal navigation bar
    )

    # Load content based on main section selected
    if selected_main == "Home":
        show_home_page()
    elif selected_main == "AI Tools":
        show_ai_tools_page()  # Subsections for AI Tools
    elif selected_main == "About":
        show_about_page()
    elif selected_main == "Contact":
        show_contact_page()


def show_ai_tools_page():
    # AI Tools Subsections
    st.markdown("<h1 class='subsection-title'>AI Tools Platform</h1>", unsafe_allow_html=True)

    selected_subsection = option_menu(
        menu_title="AI Tools",  # Subsection header
        options=["Utility Tools", "Image Tools", "Text Tools"],  # Add "None" option
        icons=["gear", "image", "pencil"],  # Icons for subsections
        menu_icon="tools",  # Icon for AI Tools
        default_index=0,  # Default subsection is "None"
        orientation="horizontal",  # Subsection bar is horizontal
    )

    # Display content based on selected subsection
    if selected_subsection == "None":
        st.write("Please select a valid tool to proceed.")
    elif selected_subsection == "Utility Tools":
        show_utility_tools()
    elif selected_subsection == "Image Tools":
        show_image_tools()
    elif selected_subsection == "Text Tools":
        show_text_tools()


def show_utility_tools():
    st.markdown("### Utility Tools")
    utility_tool = st.radio(
        "Choose a tool:", ["None", "QR Code Generator", "Resume Generator", "AI chat bot", "Word Cloud Generator", "Image Description Generator"], key="utility_tool", index=0
    )
    if utility_tool == "None":
        st.write("Please select a tool to proceed.")
    elif utility_tool == "QR Code Generator":
        qr_code_generator_page()
    elif utility_tool == "Resume Generator":
        resume_generator_page()
    elif utility_tool == "AI chat bot":
        chatbot_page()
    elif utility_tool == "Word Cloud Generator":
        wordcloud_page()
    elif utility_tool == "Image Description Generator":
        # Redirect to URL-to-Text page
        urltotext_page()


def show_image_tools():
    st.markdown("### Image Tools")
    image_tool = st.radio(
        "Select an Image Tool:",
        ["None", "Image Classification", "Image Captioning", "Object Detection"],
        key="image_tool", index=0
    )
    if image_tool == "None":
        st.write("Please select an image tool to proceed.")
    elif image_tool == "Image Classification":
        image_classification_page()
    elif image_tool == "Image Captioning":
        image_captioning_page()
    elif image_tool == "Object Detection":
        object_detection_page()


def show_text_tools():
    st.markdown("### Text Tools")
    text_tool = st.radio(
        "Choose a Text Tool:",
        ["None", "Sentiment Analysis", "Text Generation", "Text to Image"],
        key="text_tool", index=0
    )
    if text_tool == "None":
        st.write("Please select a text tool to proceed.")
    elif text_tool == "Sentiment Analysis":
        sentiment_analysis_page()
    elif text_tool == "Text Generation":
        llama_text_generation_page()
    elif text_tool == "Text to Image":
        text_to_image_page()


def show_home_page():
    st.markdown("<h1 class='title'>AI Tools Platform</h1>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to the **AI Tools Platform**, where you can explore a variety of AI-driven tools to assist with image processing, text generation, and much more. 
    Our platform provides a collection of powerful, easy-to-use AI tools for various tasks.
    Get started by exploring any of the available tools and let the AI enhance your work!
    """)

    image_url = "https://i.postimg.cc/43zVvNxp/1000350323.png"  # Replace with your image URL
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image(image_url, use_column_width=False, width=600)  # Adjust size of the image (larger size)
    st.markdown("</div>", unsafe_allow_html=True)


def show_about_page():
    st.markdown("<h1 class='title'>About</h1>", unsafe_allow_html=True)
    st.markdown("""
    AI Tools Platform is a comprehensive platform designed to showcase a variety of artificial intelligence applications.
    You can use tools for image analysis, text generation, sentiment analysis, and much more.
    Our goal is to make advanced AI tools accessible to everyone in a simple and user-friendly manner.
    """)


def show_contact_page():
    st.markdown("<h1 class='title'>Contact</h1>", unsafe_allow_html=True)
    st.markdown("""
    For any inquiries, please contact us at:
    - **Email**: [shrutianil30@gmail.com](mailto:shrutianil30@gmail.com)
    - **Linkedin**: [Shruti Shrivastav](https://www.linkedin.com/in/shruti-shrivastav-4989602b7?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
    """)


if __name__ == "__main__":
    main()


