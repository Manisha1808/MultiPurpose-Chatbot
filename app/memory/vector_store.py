import faiss
import numpy as np

from sentence_transformers import (
    SentenceTransformer
)

# FAISS setup
dimension = 384

index = faiss.IndexFlatL2(dimension)

conversation_memory = []

# Lazy model loading
embedding_model = None


def load_model():

    global embedding_model

    if embedding_model is None:

        embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return embedding_model


def store_memory(text):

    try:

        model = load_model()

        embedding = model.encode([text])

        embedding = np.array(
            embedding,
            dtype=np.float32
        )

        index.add(embedding)

        conversation_memory.append(text)

    except Exception as e:

        print("FAISS store error:", e)


def search_memory(query):

    try:

        if len(conversation_memory) == 0:
            return None

        model = load_model()

        query_embedding = model.encode([query])

        query_embedding = np.array(
            query_embedding,
            dtype=np.float32
        )

        distances, indices = index.search(
            query_embedding,
            k=3
        )

        # Return best non-identical match
        for idx in indices[0]:

            matched_text = (
                conversation_memory[idx]
            )

            if matched_text.lower().strip() != (
                query.lower().strip()
            ):

                return matched_text

        return None

    except Exception as e:

        print("FAISS search error:", e)

        return None