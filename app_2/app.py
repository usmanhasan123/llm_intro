import langchain
import transformers
import torch
import accelerate
import numpy
from langchain.llms import HuggingFaceHub
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import streamlit as st
import os
from langchain.chat_models import ChatOpenAI

# os.environ['OPENAI_API_KEY']="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"

st.set_page_config(page_title="LangChain Demo for app 2", page_icon=":robot:")
st.header("LangChain Demo for app 2")

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages=[SystemMessage(content="You are a helpful AI assisstant")] # prompt

chat = ChatOpenAI(openai_api_base="https://openrouter.ai/api/v1", openai_api_key= os.getenv("OPENAI_API_KEY"),
                 model="mistralai/Mistral-7B-Instruct", temperature=0.7)

query=st.text_input("You: ", key="input")

st.session_state.sessionMessages.append(HumanMessage(content=query))

response=chat(st.session_state.sessionMessages)
st.session_state.sessionMessages.append(AIMessage(content=response))
press=st.button("Generate response")
if press:
    st.subheader("Answer")
    st.write(response)
# response = chat.invoke("Tell me a joke!")
# print(response.content)
