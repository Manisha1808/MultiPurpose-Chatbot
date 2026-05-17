# AI-Powered Personalized Multi-Session Chatbot with Intent Detection

## Project Overview

This project is an AI-powered personalized multi-session chatbot system developed using FastAPI, Streamlit, Machine Learning, and NLP techniques. The chatbot is capable of detecting user intent, maintaining contextual memory across multiple sessions, generating intelligent responses, creating images and files based on user requests, and storing user conversation history.

The system supports personalized interactions by understanding user queries and preserving conversational continuity using database-backed session management.

The chatbot can:

* Detect user intent using Machine Learning
* Handle multi-session conversations
* Store and retrieve user chat history
* Generate AI-based responses
* Generate images based on prompts
* Generate PDF and DOCX files
* Provide an interactive frontend using Streamlit
* Expose APIs using FastAPI

---

# Features

## 1. Intent Detection

The chatbot uses a Machine Learning model to classify user queries into different intents.

Supported intents:

* Greeting
* General Query
* Image Generation
* File Generation
* Contextual Chat
* Goodbye

Machine Learning components used:

* TF-IDF Vectorizer
* Logistic Regression Classifier

---

## 2. Multi-Session Memory

The system stores:

* User ID
* Session ID
* User Messages
* Bot Responses
* Conversation History

SQLite database is used for persistent storage.

---

## 3. AI-Based Response Generation

The chatbot integrates a HuggingFace Transformer model (GPT-2) to generate AI-powered conversational responses.

---

## 4. Image Generation

The chatbot can generate images based on user prompts.

Generated images are stored in:

```text
/generated_images
```

---

## 5. PDF and DOCX File Generation

The chatbot can generate:

* PDF Notes
* Reports
* DOCX Files

Generated files are stored in:

```text
/generated_files
```

---

## 6. Frontend Interface

A Streamlit frontend provides:

* User-friendly chatbot interface
* AI response display
* Generated image display
* PDF download functionality

---

## 7. REST API Backend

FastAPI is used to expose chatbot functionality through REST APIs.

---

# Technologies Used

## Backend

* Python
* FastAPI
* Uvicorn

## Frontend

* Streamlit

## Machine Learning / NLP

* Scikit-learn
* Transformers
* GPT-2
* TF-IDF Vectorizer
* Logistic Regression

## Database

* SQLite
* SQLAlchemy

## File Generation

* ReportLab
* python-docx

## Image Generation

* Pillow

---

# Project Architecture

```text
AI-Multi-Session-Chatbot/
│
├── app/
│   ├── main.py
│   │
│   ├── services/
│   │   ├── intent_classifier.py
│   │   ├── train_intent_model.py
│   │   ├── ai_generator.py
│   │   ├── image_generator.py
│   │   ├── file_generator.py
│   │   └── memory_engine.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── models.py
│   │
│   └── memory/
│
├── frontend/
│   └── app.py
│
├── datasets/
│   └── intent_dataset.csv
│
├── trained_models/
│   ├── intent_model.pkl
│   └── vectorizer.pkl
│
├── generated_images/
├── generated_files/
│
├── requirements.txt
├── README.md
└── chatbot.db
```

---

# Dataset Information

A custom intent classification dataset was created for training the chatbot.

Dataset includes user queries for:

* Greetings
* AI-related questions
* File generation requests
* Image generation requests
* Contextual conversations
* Goodbye messages

Dataset format:

```csv
text,intent
hello,greeting
generate image,image_generation
create pdf,file_generation
bye,goodbye
```

---

# Machine Learning Model

## Intent Classification Pipeline

The chatbot uses:

1. TF-IDF Vectorization
2. Logistic Regression Classification

Training flow:

```text
User Text
   ↓
TF-IDF Vectorizer
   ↓
Logistic Regression
   ↓
Predicted Intent
```

---

# Database Design

## Conversations Table

| Column       | Description       |
| ------------ | ----------------- |
| id           | Primary Key       |
| user_id      | User Identifier   |
| session_id   | Unique Session ID |
| user_message | User Query        |
| bot_response | Chatbot Response  |

---

# API Endpoints

## Home Endpoint

### GET /

Returns server status.

Example Response:

```json
{
  "message": "AI Multi-Session Chatbot Running"
}
```

---

## Chat Endpoint

### POST /chat

Handles chatbot interaction.

Request:

```json
{
  "user_id": "manisha",
  "message": "Explain machine learning"
}
```

Response:

```json
{
  "user_id": "manisha",
  "session_id": "uuid",
  "intent": "general_query",
  "response": "Machine learning is a branch of AI..."
}
```

---

## History Endpoint

### GET /history/{user_id}

Retrieves user conversation history.

---

# Setup Instructions

## Step 1: Clone Repository

```bash
git clone <repository_url>
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Streamlit Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# Usage Guidelines

## General Chat

Example:

```text
Explain machine learning
```

---

## Image Generation

Example:

```text
generate futuristic AI image
```

Generated image appears in frontend and is stored in:

```text
/generated_images
```

---

## PDF Generation

Example:

```text
generate AI notes pdf
```

Generated file appears in frontend with download button.

Files are stored in:

```text
/generated_files
```

---

# Frontend Features

The Streamlit frontend supports:

* User ID input
* Chat interaction
* AI response rendering
* Image display
* PDF download button
* Intent display

---

# Model Training

To retrain the intent classification model:

```bash
python app/services/train_intent_model.py
```

This generates:

* intent_model.pkl
* vectorizer.pkl

inside:

```text
/trained_models
```

---

# Deployment

## GitHub Deployment

Push project to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <repo_url>
git push -u origin main
```

---

## Suggested Deployment Platforms

* Render
* Railway
* Streamlit Cloud

---

# Future Improvements

Future enhancements can include:

* FAISS Vector Database
* Semantic Search
* RAG Architecture
* OpenAI API Integration
* Authentication System
* Voice Input
* Emotion Detection
* Conversation Summarization
* Cloud Database Integration

---

# Challenges Faced

During development, several challenges were encountered:

* Python 3.13 compatibility issues with FAISS
* HuggingFace dependency compatibility
* Stable Diffusion model size limitations
* GPT-2 noisy output formatting
* Streamlit-FastAPI integration handling

These were resolved using lightweight alternatives and optimized architecture.

---

# Conclusion

The project successfully demonstrates:

* AI-powered chatbot architecture
* NLP-based intent detection
* Personalized multi-session interaction
* AI-generated responses
* File and image generation
* Database-backed memory handling
* Full-stack AI application development

This project showcases practical implementation of conversational AI systems using modern Machine Learning and NLP technologies.

---

# Author

Developed as part of the assignment:

"AI-Powered Personalized Multi-Session Chatbot with Intent Detection"
