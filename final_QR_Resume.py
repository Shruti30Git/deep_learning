import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# QR Code Generator Page
def qr_code_generator_page():
    st.title("URL to QR Code Generator")

    # User input for URL
    url = st.text_input("Enter the URL/Link:")

    # Select QR code size
    qr_size = st.slider("Select QR Code Size (pixels)", min_value=100, max_value=300, value=200, step=50)

    # Generate QR Code
    if st.button("Generate QR Code"):
        if url:
            # Use an online API to generate the QR code
            qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?data={url}&size={qr_size}x{qr_size}"
            response = requests.get(qr_api_url)

            if response.status_code == 200:
                # Convert the response content to an image
                img = Image.open(BytesIO(response.content))
                st.image(img, caption="Your QR Code", use_column_width=False)

                # Add a download button for the QR Code
                buf = BytesIO(response.content)
                st.download_button(
                    label="Download QR Code",
                    data=buf,
                    file_name="qr_code.png",
                    mime="image/png",
                )
            else:
                st.error("Failed to generate QR Code. Please try again later.")
        else:
            st.error("Please enter a valid URL!")

# Resume Generator Page
def resume_generator_page():
    st.title("Basic Resume Generator")

    # Input Fields for Resume Details
    name = st.text_input("Full Name")

    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")

    education_institution = st.text_input("Educational Institution (e.g., University Name)")
    degree = st.text_input("Degree (e.g., B.Sc., M.Sc.)")

    skills = st.multiselect(
        "Skills (select multiple skills)",
        ["Python", "Java", "C++", "JavaScript", "Data Analysis", "Machine Learning", "Web Development",
         "Cloud Computing"]
    )
    experience = st.text_area("Work Experience (Company, Role, Years)")

    age = st.number_input("Age", min_value=18, max_value=100, step=1)

    hobbies = st.selectbox("Select your hobbies",
                           ["Reading", "Traveling", "Sports", "Music", "Movies", "Gaming", "Photography", "Cooking"])

    internship_done = st.selectbox("Have you done any internship?", ["Yes", "No"])

    # Create Resume
    if st.button("Generate Resume (Scroll down to download) "):
        if name and email and phone and education_institution and degree and skills and experience and age and hobbies:
            resume_content = f"""
            <html>
            <head>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 40px;
                        padding: 20px;
                        border: 2px solid #000;
                    }}
                    h1 {{
                        text-align: center;
                        text-decoration: underline;
                    }}
                    h2 {{
                        color: #2c3e50;
                    }}
                    .content {{
                        margin: 20px;
                    }}
                    .section {{
                        margin-bottom: 15px;
                    }}
                    .declaration {{
                        margin-top: 30px;
                        font-style: italic;
                    }}
                </style>
            </head>
            <body>
                <h1>{name}'s Resume</h1>

                <div class="content">
                    <div class="section">
                        <h2>Contact Information</h2>
                        <p><strong>Email:</strong> {email}</p>
                        <p><strong>Phone:</strong> {phone}</p>
                    </div>
                    <div class="section">
                        <h2>Age</h2>
                        <p>{age} years old</p>
                    </div>
                    <div class="section">
                        <h2>Education</h2>
                        <p><strong>Institution:</strong> {education_institution}</p>
                        <p><strong>Degree:</strong> {degree}</p>
                    </div>

                    <div class="section">
                        <h2>Skills</h2>
                        <p>{', '.join(skills)}</p>
                    </div>

                    <div class="section">
                        <h2>Work Experience</h2>
                        <p>{experience}</p>
                    </div>

                    <div class="section">
                        <h2>Hobbies</h2>
                        <p>{hobbies}</p>
                    </div>

                    <div class="section">
                        <h2>Internship Experience</h2>
                        <p>{internship_done}</p>
                    </div>

                    <div class="declaration">
                        <p>I hereby declare that the above information is true to the best of my knowledge and belief.</p>
                    </div>
                </div>
            </body>
            </html>
            """

            # Display the resume in an attractive format
            st.subheader("Generated Resume")
            st.markdown(resume_content, unsafe_allow_html=True)

            # Save the HTML content to a file and allow download
            resume_html = resume_content.encode("utf-8")
            st.download_button(
                label="Download Resume",
                data=resume_html,
                file_name="resume.html",
                mime="text/html",
            )
        else:
            st.error("Please fill out all fields to generate your resume.")
