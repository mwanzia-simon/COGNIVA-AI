# Cogniva AI 

**Your knowledge. Your documents. Your AI assistant.**

Cogniva AI is a locally running AI-powered knowledge assistant that uses **Retrieval-Augmented Generation (RAG)** to answer questions using information stored in custom documents.

Instead of relying entirely on an AI model's existing knowledge, Cogniva retrieves relevant information from a document knowledge base and uses it as context to generate accurate, relevant answers.

##  Project Goal

The goal of Cogniva AI is to explore and implement the core concepts behind Retrieval-Augmented Generation while building a practical AI application that can interact with private knowledge sources locally.

##  Technologies

- **Python** – Core application logic.
- **Ollama** – Local AI model execution.
- **Qwen3:4b-instruct** – Language model for generating responses.
- **Embedding Model** – Converts text into numerical vector representations.
- **NumPy** – Vector storage, similarity calculations, and retrieval operations.
- **RAG** – Connects document retrieval with AI-generated answers.

##  How It Works

1. **Document Loading:** Reads information from the knowledge base.
2. **Text Chunking:** Divides documents into smaller, manageable sections.
3. **Embedding Generation:** Converts each text chunk into a numerical vector.
4. **Vector Storage:** Stores embeddings for later retrieval.
5. **Question Processing:** Converts the user's question into an embedding.
6. **Similarity Search:** Finds the document chunks most relevant to the question.
7. **Answer Generation:** Sends the retrieved context and question to the language model.
8. **Response:** Generates an answer grounded in the retrieved information.

##  Knowledge Base

The initial knowledge base uses a fictional technology company, **Unlisted Code Logic**, to simulate a real-world business information system.

It contains company information, employee records, services, projects, internal policies, financial information, and operational documentation.

This provides information that the AI cannot reliably answer from general knowledge alone.

##  Project Status

**Currently in development.**

Planned improvements include:
- Document ingestion and processing.
- Efficient vector similarity search.
- Improved retrieval accuracy.
- Context-aware response generation.
- Support for additional document formats.
- Interactive question-and-answer interface.

##  Learning Objectives

This project is also a practical exploration of:

- Retrieval-Augmented Generation.
- Natural Language Processing.
- Text embeddings and vector representations.
- Cosine similarity.
- Semantic search.
- Local Large Language Models (LLMs).
- AI application development.

##  Local AI Approach

Cogniva AI is designed to run locally using Ollama, reducing dependence on external AI APIs and allowing documents to remain on the local machine during processing, subject to the application's configuration.

##  Developer

Developed by **Simon Makau** under the technology brand **Unlisted Code Logic**.

---

*Building intelligent systems, one concept at a time.*