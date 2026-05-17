from fastapi import FastAPI
from pydantic import BaseModel
import uuid

from app.database.db import engine
from app.database.models import Base

from app.services.intent_classifier import predict_intent

from app.services.memory_engine import (
    save_conversation,
    get_conversation_history
)

from app.services.ai_generator import (
    generate_ai_response
)

from app.services.image_generator import (
    generate_image
)
from app.services.file_generator import (
    generate_pdf,
    generate_docx
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.get("/")
def home():
    return {
        "message": "AI Multi-Session Chatbot Running"
    }


@app.post("/chat")
def chatbot(chat_request: ChatRequest):

    # Generate session ID
    session_id = str(uuid.uuid4())

    # Predict intent
    intent = predict_intent(
        chat_request.message
    )

    # Image generation
    if intent == "image_generation":

        image_path = generate_image(
            chat_request.message
        )

        bot_response = (
            f"Image generated successfully: "
            f"{image_path}"
        )

    # Normal AI response
    # File generation
    elif intent == "file_generation":

       ai_content = f"""
AI Generated Notes

       Topic: {chat_request.message}

    Artificial Intelligence (AI) is a branch
    of computer science that enables systems
    to simulate human intelligence.

    Machine Learning is a subset of AI that
    allows systems to learn from data.

    Deep Learning uses neural networks for
    advanced pattern recognition.

    Applications:
    - Chatbots
    - Healthcare
    - Finance
    - Robotics
       
    """

       pdf_path = generate_pdf(
       ai_content,
        "generated_report"
    )

       bot_response = (
        f"PDF generated successfully: "
        f"{pdf_path}"
    )

# Normal AI response
    else:

       bot_response = generate_ai_response(
        chat_request.message
    )



    # Save conversation
    save_conversation(
        user_id=chat_request.user_id,
        session_id=session_id,
        user_message=chat_request.message,
        bot_response=bot_response
    )

    return {
        "user_id": chat_request.user_id,
        "session_id": session_id,
        "message": chat_request.message,
        "intent": intent,
        "response": bot_response
    }


@app.get("/history/{user_id}")
def history(user_id: str):

    chats = get_conversation_history(user_id)

    results = []

    for chat in chats:

        results.append({
            "session_id": chat.session_id,
            "user_message": chat.user_message,
            "bot_response": chat.bot_response
        })

    return results