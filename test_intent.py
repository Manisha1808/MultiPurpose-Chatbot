from app.services.intent_classifier import predict_intent

text = input("Enter message: ")

intent = predict_intent(text)

print("Predicted Intent:", intent)