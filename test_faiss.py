from app.memory.vector_store import (
    store_memory,
    search_memory
)

# Store conversations
store_memory("I like AI projects")

store_memory("Machine learning is interesting")

store_memory("Python is my favorite language")

# Search related memory
query = "Tell me about artificial intelligence"

result = search_memory(query)

print("Matched Memory:")
print(result)