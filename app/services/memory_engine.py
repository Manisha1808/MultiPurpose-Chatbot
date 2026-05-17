from app.database.db import SessionLocal
from app.database.models import Conversation


def save_conversation(
    user_id,
    session_id,
    user_message,
    bot_response
):

    db = SessionLocal()

    conversation = Conversation(
        user_id=user_id,
        session_id=session_id,
        user_message=user_message,
        bot_response=bot_response
    )

    db.add(conversation)

    db.commit()

    db.close()


def get_conversation_history(user_id):

    db = SessionLocal()

    chats = db.query(Conversation).filter(
        Conversation.user_id == user_id
    ).all()

    db.close()

    return chats


def get_last_conversation(user_id):

    db = SessionLocal()

    last_chat = db.query(Conversation).filter(
        Conversation.user_id == user_id
    ).order_by(Conversation.id.desc()).first()

    db.close()

    return last_chat