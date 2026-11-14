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


# Breaking the document into chunks
chunks = []
for file in Path("docs").glob("*.md"):
    chunks += [p.strip() for p in file.read_text(encoding="utf-8").split("\n\n") if p.strip()]
    
    
# Vectorizing the chunks list
chunk_vectors = embed(chunks)

# function to find similarity between the chunks returning the 3 closest chunks
def retrieve(question, k=3):
    q = embed(question).reshape(-1)
    scores = chunk_vectors @ q / (np.linalg.norm(chunk_vectors,axis=1) * np.linalg.norm(q))
    return [chunks[i] for i in np.argsort(scores)[::-1][:k]]

# Giving the llm the context before answering the questions
while True:
    question = input("ASK: ")
    context = "\n\n".join(retrieve(question))
    prompt = f"""
    Answer the question using ONLY the context below.
    if the answer isn't in the context, say "I don't know".
    Context: {context}
    Question: {question}"""
    print("\n" + ask_llm(prompt) + "\n")
    