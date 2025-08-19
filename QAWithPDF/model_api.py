import os
from dotenv import load_dotenv
import sys

from llama_index.llms.gemini import Gemini
from IPython.display import display, Markdown
import google.generativeai as genai
from exception import customexception
from logger import logging

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def load_model():
    try:
        logging.info("Model loading started")
        model = Gemini(model="gemini-1.5-flash")
        logging.info("Model loading completed")
        return model
    except Exception as e:
        logging.info("Model loading failed")
        raise customexception(e, sys)