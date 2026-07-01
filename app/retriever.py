from app.vector_store import create_or_load_vectorstore

db = create_or_load_vectorstore()

def retrieve(query, k=3):
    return db.similarity_search(query, k=k)