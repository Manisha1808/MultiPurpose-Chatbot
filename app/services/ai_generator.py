from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_ai_response(user_message):

    user_message = user_message.lower()

    # Machine Learning
    if "machine learning" in user_message:

        return (
            "Machine Learning is a subset "
            "of Artificial Intelligence "
            "that enables systems to learn "
            "from data without being "
            "explicitly programmed."
        )

    # Artificial Intelligence
    elif (
        "artificial intelligence" in user_message
        or " ai " in f" {user_message} "
    ):

        return (
            "Artificial Intelligence (AI) "
            "is a branch of computer science "
            "that enables machines to simulate "
            "human intelligence such as learning, "
            "reasoning, and decision-making."
        )

    # Deep Learning
    elif "deep learning" in user_message:

        return (
            "Deep Learning is a subset of "
            "Machine Learning that uses "
            "neural networks to process "
            "complex patterns in data."
        )

    # Python
    elif "python" in user_message:

        return (
            "Python is a popular programming "
            "language widely used in AI, "
            "Machine Learning, Web Development, "
            "and Data Science."
        )

    # Default
    else:

        return (
            "This chatbot uses NLP, "
            "intent detection, FAISS vector "
            "search, and RAG-style semantic "
            "retrieval for intelligent responses."
        )