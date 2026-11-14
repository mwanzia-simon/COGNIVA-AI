import requests
import numpy as np
from pathlib import path

OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen3:4b-instruct"


# Function to embed text
def embed(texts):
    r = requests.post(f"{OLLAMA}/api/embed",json={"model":EMBED_MODEL,"input":texts})
    return np.array(r.json()["embeddings"])