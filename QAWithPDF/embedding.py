from llama_index.core import VectorStoreIndex, Settings
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
import os


from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model,document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("")
        gemini_embed_model = GeminiEmbedding(model_name="models/gemini-embedding-001")

        # Service context

        logging.info("")
        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 80

        # Create index
        index = VectorStoreIndex.from_documents(document)

        PERSIST_DIR = "./storage"

        # Step 2: Check if index exists
        if not os.path.exists(PERSIST_DIR):
            print("🔹 First time: Creating index...")

            # Save index
            index.storage_context.persist(persist_dir=PERSIST_DIR)

        else:
            print("🔹 Loading existing index...")

            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
        
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)