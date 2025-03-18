import langchain
import huggingface_hub
from langchain.embeddings import HuggingFaceHubEmbeddings
import os
import transformers
from streamlit import st

embeddings=HuggingFaceHubEmbeddings()

st.set_page_config("Langchain demo for text embeddings", page_icon=":robot:")
st.header("Langchain demo for text embeddings")

embeddings=HuggingFaceHubEmbeddings()

text=st.text_input("You: ", key="input")

sents=nltk.sent_tokenize(text)
embed_list=[]
for sent in sents:
    embed=embeddings.embed_query(sent.lower())
    embed_list.append(embed)
    
sim_list=[]
for i, sent in enumerate(sents):
    twod_emed=np.array(embed_list[i]).reshape(1,-1)
    sim=cosine_similarity(np.array(embed_list[0]).reshape(1,-1), twod_emed)
    sim_list.append(sim)
    
df_sent=pd.DataFrame({"sents": sents, "embeddings": embed_list, "cos_sim": sim_list})
df_sent["cos_sim"]=df_sent.apply(lambda x: x["cos_sim"][0][0], axis=1)
df_sent=df_sent.sort_values(by="cos_sim", ascending=False)
summary=""

words=st.text_input("summary words: ", key="input")

for i in df_sent["sents"][:words]:
    summary=summary+i
    summary=summary+" "
    
press=st.button("Generate summary")
if press:
    st.subheader("Summary")
    st.write(summary)
