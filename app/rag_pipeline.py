from app.retriever import retrieve
from app.llm import generate_response


def ask(query: str):
    docs = retrieve(query)
    return generate_response(query, docs)