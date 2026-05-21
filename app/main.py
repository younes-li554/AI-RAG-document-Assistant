import tempfile
import streamlit as st

from utils.text_splitter import split_documents
from utils.document_loader import load_document

from models.embedding_model import load_embedding_model
from models.llm_model import load_llm

from rag.vector_store import create_vector_store
from rag.rag_chain import build_rag_chain


# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="AI Agentic Document Assistant",
    layout="wide"
)

st.title("📄 AI Agentic Document Assistant")


# =========================
# SESSION STATE INITIALIZATION
# =========================
# Store vector database to avoid recomputation
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# Store RAG chain for reuse
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None


# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "Upload PDF or TXT File",
    type=["pdf", "txt"]
)


# =========================
# MAIN PIPELINE
# =========================
if uploaded_file:

    st.success("File Uploaded Successfully ✅")

    # Save uploaded file temporarily on disk
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    # Load document from file
    documents = load_document(file_path, uploaded_file.name)

    # Split document into chunks for embedding
    chunks = split_documents(documents)

    st.subheader("Document Loaded")
    st.write(f"Total Chunks: {len(chunks)}")

    # Optional: Show document chunks for debugging
    with st.expander("Show Document Chunks"):
        for i, chunk in enumerate(chunks):
            st.markdown(f"**Chunk {i+1}**")
            st.write(chunk.page_content)


    # =========================
    # EMBEDDING MODEL
    # =========================
    with st.spinner("Loading Embedding Model..."):
        embeddings = load_embedding_model()

    st.success("Embeddings Loaded Successfully ✅")


    # =========================
    # VECTOR STORE (FAISS)
    # =========================
    if st.session_state.vectorstore is None:

        with st.spinner("Creating Vector Store..."):
            st.session_state.vectorstore = create_vector_store(
                chunks,
                embeddings
            )

        st.success("Vector Store Ready 🚀")


    # =========================
    # LOAD LLM (Gemini / Cloud Model)
    # =========================
    with st.spinner("Loading LLM..."):
        llm = load_llm()


    # =========================
    # BUILD RAG CHAIN (ONLY ONCE)
    # =========================
    if st.session_state.rag_chain is None:

        with st.spinner("Building RAG System..."):
            st.session_state.rag_chain = build_rag_chain(
                st.session_state.vectorstore,
                llm
            )

        st.success("RAG System Ready 🚀")


    # =========================
    # CHAT INPUT
    # =========================
    query = st.chat_input("Ask a question from your document...")


    if query:

        # Show user question immediately
        st.subheader("Question")
        st.write(query)

        # =========================
        # GENERATE ANSWER
        # =========================
        with st.spinner("Generating Answer... 🤔"):
            response = st.session_state.rag_chain.invoke(query)

        # Display answer
        st.subheader("AI Answer")
        st.write(response)