import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/chat"

# Page config
st.set_page_config(
    page_title="AI Multi-Session Chatbot",
    layout="centered"
)

# Title
st.title("AI Multi-Session Chatbot")

# User ID input
user_id = st.text_input(
    "Enter User ID",
    value="manisha"
)

# Message input
message = st.text_input(
    "Enter your message"
)

# Send button
if st.button("Send"):

    # Empty message check
    if not message.strip():

        st.warning(
            "Please enter a message."
        )

    else:

        payload = {

            "user_id": user_id,
            "message": message
        }

        try:

            # API request
            response = requests.post(
                API_URL,
                json=payload
            )

            data = response.json()

            response_text = data["response"]

            # -------------------------
            # BOT RESPONSE
            # -------------------------

            st.subheader("Bot Response")

            st.write(response_text)

            # -------------------------
            # DETECTED INTENT
            # -------------------------

            st.subheader("Detected Intent")

            st.write(data["intent"])

            # -------------------------
            # IMAGE DISPLAY
            # -------------------------

            if "generated_images/" in response_text:

                image_path = (
                    response_text.split(": ")[1]
                    .split("\n")[0]
                    .strip()
                )

                st.image(
                    image_path,
                    caption="Generated Image"
                )

            # -------------------------
            # FILE DOWNLOAD
            # -------------------------

            if "generated_files/" in response_text:

                file_path = (
                    response_text.split(": ")[1]
                    .split("\n")[0]
                    .strip()
                )

                with open(file_path, "rb") as file:

                    st.download_button(
                        label="Download File",
                        data=file,
                        file_name=file_path.split("/")[-1]
                    )

        except Exception as e:

            st.error(
                f"Error connecting to backend: {e}"
            )