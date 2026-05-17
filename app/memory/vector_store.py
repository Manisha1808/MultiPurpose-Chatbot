import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# FAISS index
dimension = 384

index = faiss.IndexFlatL2(dimension)

# Store actual conversations
conversation_memory = []

def store_memory(text):

    # Convert text to embedding
    embedding = embedding_model.encode([text])

    embedding = np.array(
        embedding,
        dtype=np.float32
    )

    # Add embedding to FAISS
    index.add(embedding)

    # Save text memory
    conversation_memory.append(text)

def search_memory(query):

    # No memory yet
    if len(conversation_memory) == 0:
        return None

    # Query embedding
    query_embedding = embedding_model.encode([query])

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    # Search FAISS
    distances, indices = index.search(
        query_embedding,
        k=1
    )

    matched_index = indices[0][0]

    return conversation_memory[matched_index]