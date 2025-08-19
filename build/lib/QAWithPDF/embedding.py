from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding():
    try:
        logging.info("Gemini embedding download started")
        gemini_embed_model = GeminiEmbedding()
        logging.info("Gemini embedding download completed")
        return gemini_embed_model
    except Exception as e:
        logging.info("Gemini embedding download failed")
        raise customexception(e, sys)