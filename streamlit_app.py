import streamlit as st
from app.rag_pipeline import ask

st.set_page_config(page_title="SHL AI Assistant", layout="centered")

st.title("🤖 SHL AI Assistant (RAG System)")
st.write("Ask me to recommend SHL assessments based on job roles or skills.")

# Input box
query = st.text_input("Enter your query")

if st.button("Get Recommendation"):
    if query.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking... "):
            response = ask(query)

        st.success("Response")
        st.write(response)