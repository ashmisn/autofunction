import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import normalize

# Load embedding model
model = SentenceTransformer("all-mpnet-base-v2")  # More powerful than MiniLM

# Define function descriptions
function_descriptions = {
    "open_chrome": "Launch Google Chrome browser",
    "open_calculator": "Start the calculator application",
    "get_cpu_usage": "Fetch CPU usage percentage",
    "execute_command": "Run a terminal command"
}

# Convert descriptions into embeddings
descriptions = list(function_descriptions.values())
embeddings = model.encode(descriptions)

# Normalize embeddings for cosine similarity
embeddings = normalize(embeddings, axis=1, norm='l2')

# Store embeddings in FAISS using Inner Product (cosine similarity)
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

# Function to retrieve the best-matching function
def retrieve_function(user_query):
    user_embedding = model.encode([user_query])  # Convert input to embedding
    user_embedding = normalize(user_embedding, axis=1, norm='l2')  # Normalize for cosine similarity
    
    distances, indices = index.search(user_embedding, 1)  # Find closest match
    
    best_match = list(function_descriptions.keys())[indices[0][0]]
    return best_match
