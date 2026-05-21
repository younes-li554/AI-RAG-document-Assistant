from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

def load_document(file_path, file_name):

    if file_name.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    elif file_name.endswith(".txt"):
        loader = TextLoader(file_path)

    else:
        raise ValueError("Unsupported file format")

    documents = loader.load()

    return documents