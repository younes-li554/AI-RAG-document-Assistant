from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

@st.cache_resource
def load_embedding_model():

    model_name = os.getenv("EMBEDDING_MODEL")

    embeddings = HuggingFaceEmbeddings(
        model_name=model_name
    )

    return embeddings