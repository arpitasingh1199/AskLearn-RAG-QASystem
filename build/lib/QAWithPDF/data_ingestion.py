from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data):

    try:
        model=Gemini(models='gemini-pro',api_key=GOOGLE_API_KEY)
        return model
    except Exception as e:
        raise customexception(e,sys)
        