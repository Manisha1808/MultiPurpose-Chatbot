import joblib

# Load saved model
model = joblib.load("trained_models/intent_model.pkl")

# Load vectorizer
vectorizer = joblib.load("trained_models/vectorizer.pkl")


def predict_intent(text):

    # Convert text to vector
    text_vector = vectorizer.transform([text])

    # Predict
    prediction = model.predict(text_vector)

    return prediction[0]