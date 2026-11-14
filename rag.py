import requests
import numpy as np
from pathlib import Path

OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen3:4b-instruct"


# Function to embed text
def embed(texts):
    r = requests.post(f"{OLLAMA}/api/embed",json={
        "model":EMBED_MODEL,
        "input":texts
        })
    return np.array(r.json()["embeddings"])

# Function to chat with llm
def ask_llm(prompt):
    r = requests.post(f"{OLLAMA}/api/chat",json={
        "model":CHAT_MODEL,
        "stream":False,
        "messages":[{"role":"user","content":prompt}]
    })
    return r.json()["message"]["content"]


chunks = []
for file in Path("docs").glob("*.md"):
    chunks += [p.strip() for p in file.read_text(encoding="utf-8").split("\n\n") if p.strip()]