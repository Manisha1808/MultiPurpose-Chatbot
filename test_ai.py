from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)


def generate_ai_response(user_message):

    response = generator(
        user_message,
        max_new_tokens=40,
        truncation=True
    )

    generated_text = response[0]["generated_text"]

    return generated_text