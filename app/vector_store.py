import os
# from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.load_catalog import load_catalog

PERSIST_DIR = "chroma_db"

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def create_or_load_vectorstore():

    if os.path.exists(PERSIST_DIR):
        return Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=embedding
        )

    docs = load_catalog()

    db = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory=PERSIST_DIR
    )

    return db