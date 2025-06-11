Agentic RAG System with LangGraph, Azure OpenAI, and Weaviate
Overview

This project implements a Retrieval-Augmented Generation (RAG) system using:

    Weaviate (vector database for document storage and retrieval)

    Azure OpenAI (GPT-4o) for answer generation, self-critique, and refinement

    LangGraph for node-based orchestration of the RAG pipeline

The system retrieves relevant knowledge snippets, generates an answer, critiques itself, and refines the answer if needed.
Workflow

    Data Preparation & Ingestion

        Embed your documents/snippets using Azure OpenAI embeddings (text-embedding-ada-002).

        Upsert these embeddings and metadata (doc_id, answer_snippet, source, etc.) into Weaviate.

    Agentic RAG Pipeline (LangGraph)

        Retriever Node: Finds top 5 relevant KB snippets using vector search.

        LLM Answer Node: Uses GPT-4o to generate an answer citing the retrieved snippets.

        Self-Critique Node: LLM checks if the answer is complete. If not, lists missing points.

        Refinement Node: Retrieves more info if needed, and LLM refines the answer.

        Control Flow: Returns initial or refined answer based on self-critique.

    Robustness

        Logging for every pipeline step.

        Retries for LLM and retrieval calls.

Requirements

    Python 3.8+

    openai

    weaviate-client

    langgraph

    tenacity

    python-dotenv for loading environment variables

Usage

    Configure environment variables:

        Azure OpenAI and Weaviate keys/endpoints

    Run the embedding & ingestion script to populate Weaviate.

    Run the main pipeline notebook or script to ask questions and see the agentic RAG flow in action.

    Check logs and outputs for KB hits, answer, critique, and refinement details.

Example

question = "What should I consider for error handling?"
response = agentic_rag_qa(question)
print(response)

Sample output:

KB Hits: ['KB009', 'KB019']
Initial Answer: [ ...cites [KB009]... ]
Critique: COMPLETE
Answer was not refined.
{'answer': '...final answer...'}

Notes

    Update the retrieval logic if your KB structure changes.

    The system supports any Azure OpenAI GPT deployment for text generation.

    For production use, further enhance error handling and monitoring as needed.

Happy RAGging! 🚀