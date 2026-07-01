import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_response(query, docs):

    context = ""

    for doc in docs:
        context += f"""
Name: {doc.metadata.get('name')}
URL: {doc.metadata.get('url')}
Description:
{doc.page_content}
-------------------
"""

    prompt = f"""
You are an SHL assessment recommendation assistant.

Use ONLY the context below.

Context:
{context}

User Query:
{query}

Return best matching assessments with explanation.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content