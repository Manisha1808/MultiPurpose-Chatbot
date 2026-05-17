import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="AI Multi-Session Chatbot",
    layout="centered"
)

st.title("AI Multi-Session Chatbot")

# User ID
user_id = st.text_input(
    "Enter User ID",
    value="manisha"
)

# User message
message = st.text_input(
    "Enter your message"
)

# Send button
if st.button("Send"):

    payload = {
        "user_id": user_id,
        "message": message
    }

    # API request
    response = requests.post(
        API_URL,
        json=payload
    )

    data = response.json()

    response_text = data["response"]

    # Bot response
    st.subheader("Bot Response")

    st.write(response_text)

    # Detected intent
    st.subheader("Detected Intent")

    st.write(data["intent"])

    # Display generated image
    if "generated_images/" in response_text:

        image_path = (
            response_text.split(": ")[1]
        )

        st.image(
            image_path,
            caption="Generated Image"
        )

    # Download generated files
    if "generated_files/" in response_text:

        file_path = (
            response_text.split(": ")[1]
        )

        with open(file_path, "rb") as file:

            st.download_button(
                label="Download File",
                data=file,
                file_name=file_path.split("/")[-1]
            )