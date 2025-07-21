import streamlit as st
import huggingface_hub
from langchain.llms import HuggingFaceHub
import os

# os.system("git clone https://github.com/usmanhasan123/llm_intro.git")

api_key=st.secrets["HUGGINGFACEHUB_API_TOKEN"]
st.set_page_config(page_title="Langchain demo", page_icon=":robot:")
st.header("Langchain Demo")
llm=HuggingFaceHub(repo_id="google/gemma-2-2b-it", huggingfacehub_api_token=api_key)
query=st.text_input("You: ", key="input")
press=st.button("Generate")
if press:
    st.subheader("Answer: ")
    response=llm(query)
    st.write(response)
