import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.settings import Settings

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model
from exception import customexception
from logger import logging

PERSIST_DIR = "./local_db"  # Folder for storing index

def download_gemini_embedding(model, documents):
    """
    Loads an existing VectorStoreIndex if available and updates it with new documents.
    If no index exists, creates a new one and persists it.
    """
    try:
        logging.info("Initializing Gemini embedding model...")
        gemini_embed_model = GeminiEmbedding(model_name="models/embedding-001")

        Settings.llm = model
        Settings.embed_model = gemini_embed_model
        Settings.chunk_size = 800
        Settings.chunk_overlap = 20

        # Flatten list if nested
        if any(isinstance(d, list) for d in documents):
            documents = [item for sublist in documents for item in sublist]

        if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
            logging.info("Loading existing index from local storage...")
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)

            if documents:
                logging.info(f"Adding {len(documents)} new documents to index...")
                for doc in documents:
                    index.insert(doc)
                index.storage_context.persist(persist_dir=PERSIST_DIR)
        else:
            logging.info("Creating new VectorStoreIndex...")
            index = VectorStoreIndex.from_documents(documents)
            logging.info("Persisting index to local storage...")
            index.storage_context.persist(persist_dir=PERSIST_DIR)

        logging.info("Creating query engine...")
        return index.as_query_engine()

    except Exception as e:
        raise customexception(e, sys)

def load_existing_index():
    """
    Loads an already persisted index from ./local_db
    """
    try:
        if not os.path.exists("./local_db"):
            raise FileNotFoundError("No local database found. Please embed documents first.")

        logging.info("Loading existing index from local storage...")
        storage_context = StorageContext.from_defaults(persist_dir="./local_db")
        index = load_index_from_storage(storage_context)

        return index.as_query_engine()

    except Exception as e:
        raise customexception(e, sys)
