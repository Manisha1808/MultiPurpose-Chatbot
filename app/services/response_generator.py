def generate_response(intent, message, history):

    # Greeting responses
    if intent == "greeting":
        return "Hello! How can I help you today?"

    # General queries
    elif intent == "general_query":
        return f"You asked: '{message}'. I will help you with that."

    # Image generation
    elif intent == "image_generation":
        return f"Generating image for: '{message}'"

    # File generation
    elif intent == "file_generation":
        return f"Generating file for: '{message}'"

    # Contextual chat
    elif intent == "contextual_chat":

        if len(history) > 0:

            last_chat = history[-1]

            return (
                f"Previously you said: "
                f"'{last_chat.user_message}'"
            )

        else:
            return "No previous conversation found."

    # Goodbye
    elif intent == "goodbye":
        return "Goodbye! Have a great day."

    return "I'm not sure how to respond."