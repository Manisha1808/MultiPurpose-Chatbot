from sqlalchemy import Column, Integer, String, Text
from app.database.db import Base


class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(String)

    session_id = Column(String)

    user_message = Column(Text)

    bot_response = Column(Text)