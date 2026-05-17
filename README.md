# AI-Powered Personalized Multi-Session Chatbot with Intent Detection and RAG-Based Semantic Memory

## Project Overview

This project is an AI-powered personalized multi-session chatbot system developed using FastAPI, Streamlit, Machine Learning, NLP, and Retrieval-Augmented Generation (RAG) concepts.

The chatbot is capable of:
- Detecting user intent
- Maintaining contextual memory across multiple sessions
- Generating intelligent responses
- Performing semantic search using FAISS vector database
- Generating images and files
- Preserving contextual continuity using vector embeddings and conversation history

The system supports personalized interactions by understanding user preferences, previous queries, semantic similarity, and conversational history.

---

# Features

## 1. Intent Detection

The chatbot uses a Machine Learning model to classify user queries into different intents.

Supported intents:
- Greeting
- General Query
- Image Generation
- File Generation
- Contextual Chat
- Goodbye

Machine Learning components used:
- TF-IDF Vectorizer
- Logistic Regression Classifier

---

## 2. Multi-Session Memory

The chatbot maintains contextual continuity across sessions using:
- User IDs
- Session IDs
- SQLite conversation storage
- Semantic retrieval memory

The system stores:
- User messages
- Bot responses
- Session history
- Contextual memory

---

## 3. Semantic Search and RAG-Based Retrieval

The chatbot implements a lightweight Retrieval-Augmented Generation (RAG) pipeline.

Workflow:

```text
User Query
    ↓
SentenceTransformer Embedding
    ↓
FAISS Vector Search
    ↓
Retrieve Relevant Memory
    ↓
Generate Context-Aware Response
```

The system uses:
- SentenceTransformer embeddings
- FAISS vector database
- Semantic similarity search
- Context-aware memory retrieval

This enables:
- Personalized conversations
- Semantic contextual continuity
- Intelligent memory retrieval

---

# 4. AI-Based Response Generation

The chatbot generates AI responses using:
- NLP-based response generation
- Template-based intelligent responses
- Semantic memory augmentation

---

# 5. Image Generation

The chatbot can generate images based on user prompts.

Generated images are stored in:

```text
/generated_images
```

---

# 6. PDF and DOCX File Generation

The chatbot can generate:
- PDF Notes
- Reports
- DOCX Files

Generated files are stored in:

```text
/generated_files
```

---

# 7. Streamlit Frontend Interface

The Streamlit frontend provides:
- Chat interface
- User interaction
- AI response rendering
- Generated image display
- PDF download support
- Intent display
- Multi-session interaction

---

# 8. REST API Backend

FastAPI is used to expose chatbot functionality through REST APIs.

The backend handles:
- Intent detection
- AI response generation
- Semantic retrieval
- Database operations
- Image generation
- File generation

---

# Technologies Used

## Backend
- Python
- FastAPI
- Uvicorn

## Frontend
- Streamlit

## Machine Learning / NLP
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- SentenceTransformers
- Transformers
- NLP Techniques

## Vector Database / RAG
- FAISS
- Semantic Search
- Vector Embeddings
- RAG-style Retrieval

## Database
- SQLite
- SQLAlchemy

## File Generation
- ReportLab
- python-docx

## Image Generation
- Pillow

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
│       └── vector_store.py
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
├── .gitignore
└── chatbot.db
```

---

# Dataset Information

A custom intent classification dataset was created for training the chatbot.

Dataset categories include:
- Greetings
- AI-related queries
- Image generation requests
- File generation requests
- Contextual conversations
- Goodbye messages

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

# Semantic Retrieval Pipeline

The chatbot uses embedding-based semantic retrieval.

Pipeline:

```text
Conversation Text
      ↓
SentenceTransformer Embedding
      ↓
FAISS Vector Index
      ↓
Semantic Similarity Search
      ↓
Relevant Memory Retrieval
```

This enables:
- Context-aware conversations
- Personalized responses
- RAG-style memory augmentation

---

# Database Design

## Conversations Table

| Column | Description |
|---|---|
| id | Primary Key |
| user_id | User Identifier |
| session_id | Unique Session ID |
| user_message | User Query |
| bot_response | Chatbot Response |

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
  "message": "Tell me about Artificial Intelligence"
}
```

Response:

```json
{
  "user_id": "manisha",
  "session_id": "uuid",
  "intent": "general_query",
  "response": "Artificial Intelligence (AI) is a branch of computer science..."
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

## General AI Chat

Example:

```text
Tell me about Artificial Intelligence
```

---

## Semantic Search / RAG Demo

### First Query

```text
I love Artificial Intelligence
```

### Second Query

```text
Tell me about AI
```

Expected:
- Semantic memory retrieval
- Relevant contextual memory display

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

Generated file appears in frontend with download support.

Files are stored in:

```text
/generated_files
```

---

# Frontend Features

The Streamlit frontend supports:
- User ID input
- Chat interaction
- AI response rendering
- Image display
- PDF download button
- Intent display
- Error handling
- Multi-session interaction

---

# Model Training

To retrain the intent classification model:

```bash
python app/services/train_intent_model.py
```

This generates:
- intent_model.pkl
- vectorizer.pkl

inside:

```text
/trained_models
```

---

# GitHub Deployment

Push project to GitHub:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repository_url>
git push -u origin main
```

---

# Suggested Deployment Platforms

- Render
- Railway
- Streamlit Cloud

---

# Challenges Faced

During development, several challenges were encountered:

- Python 3.13 compatibility issues with FAISS
- SentenceTransformer dependency handling
- HuggingFace model loading issues
- Stable Diffusion model size limitations
- GPT-2 noisy response generation
- Streamlit-FastAPI integration handling
- Semantic retrieval optimization

These were resolved using:
- Lazy loading techniques
- Error-safe FAISS integration
- Lightweight semantic retrieval
- Optimized frontend/backend architecture

---

# Future Improvements

Future enhancements can include:
- OpenAI API Integration
- Authentication System
- Voice Input
- Emotion Detection
- Cloud Database Integration
- Conversation Summarization
- Real-time Web Search
- Advanced LLM Integration
- Multi-user Authentication

---

# Conclusion

The project successfully demonstrates:

- NLP-based intent detection
- Personalized multi-session conversations
- FAISS-based semantic retrieval
- RAG-style contextual memory
- AI-generated responses
- Vector embedding search
- Image generation
- PDF and DOCX generation
- Database-backed memory handling
- Full-stack AI application development

The project integrates NLP, intent detection, semantic vector retrieval, and RAG-style memory augmentation to build an intelligent context-aware conversational AI system.

This project showcases practical implementation of modern Generative AI concepts including:
- Vector databases
- Embedding-based retrieval
- Semantic search
- Retrieval-Augmented Generation (RAG)
- Conversational AI systems

---

# Author

Developed as part of the assignment:

AI-Powered Personalized Multi-Session Chatbot with Intent Detection
