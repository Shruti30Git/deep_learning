import streamlit as st
import requests

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": "Bearer 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"}  # Replace with your Hugging Face API key


# Function to query the Hugging Face API
def query_huggingface(model, messages, max_tokens=500):
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API Error: {response.status_code} - {response.text}")
        return None


# Page function for chatbot
def chatbot_page():
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "user_input" not in st.session_state:
        st.session_state["user_input"] = ""

    # Title and instructions
    st.title("AI Chatbot")
    st.markdown("Chat with the **Qwen2.5-Coder-32B-Instruct** model powered by Hugging Face.")

    # Function to handle user input and update the chat
    def handle_input():
        user_input = st.session_state.user_input
        if user_input.strip():  # Check for non-empty input
            st.session_state["messages"].append({"role": "user", "content": user_input})

            # Query the Hugging Face API for a response
            try:
                response = query_huggingface(
                    model="Qwen/Qwen2.5-Coder-32B-Instruct",
                    messages=st.session_state["messages"]
                )
                if response:
                    reply = response["choices"][0]["message"]["content"]
                    st.session_state["messages"].append({"role": "assistant", "content": reply})
            except Exception as e:
                st.session_state["messages"].append(
                    {"role": "assistant", "content": f"An error occurred: {e}"}
                )

            # Clear the input box after processing
            st.session_state.user_input = ""

    # "New Chat" button
    if st.button("New Chat"):
        st.session_state["messages"] = []
        st.success("Started a new chat!")

    # Chat history display
    st.markdown("### Chat History")
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        elif msg["role"] == "assistant":
            st.markdown(f"**AI:** {msg['content']}")

    # Input box for user message (triggered on change)
    st.text_input(
        "You:",
        value=st.session_state.user_input,
        placeholder="Type your message here and press Enter...",
        key="user_input",
        on_change=handle_input,
    )


