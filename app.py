import streamlit as st
import huggingface_hub
from langchain.llms import HuggingFaceHub

st.set_page_config(page_title="Langchain demo", page_icon=":robot:")
st.header("Langchain Demo")
llm=HuggingFaceHub(repo_id="google/gemma-2-2b-it")
query=st.text_input("You: ", key="input")
press=st.button("Generate")
if press:
    st.subheader("Answer: ")
    response=llm(query)
    st.write(response)
