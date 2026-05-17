import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("datasets/intent_dataset.csv")

# Inputs and labels
X = df["text"]
y = df["intent"]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()

model.fit(X_vectorized, y)

# Save vectorizer
joblib.dump(vectorizer, "trained_models/vectorizer.pkl")

# Save model
joblib.dump(model, "trained_models/intent_model.pkl")

print("Model trained and saved successfully!")