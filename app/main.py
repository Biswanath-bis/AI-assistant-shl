from fastapi import FastAPI
from pydantic import BaseModel

from app.retriever import retrieve
from app.llm import generate_response

app = FastAPI(title="SHL AI Assistant")


@app.get("/")
def root():
    return {"message": "SHL AI Assistant running"}


@app.get("/health")
def health():
    return {"status": "ok"}


class QueryRequest(BaseModel):
    query: str


@app.post("/chat")
def chat(request: QueryRequest):
    docs = retrieve(request.query)
    answer = generate_response(request.query, docs)

    return {
        "query": request.query,
        "response": answer
    }