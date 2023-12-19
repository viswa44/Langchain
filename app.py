from langchain.llms import openai
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
######### load openai model and get responses
def get_openai_response(question):
    llm = openai.OpenAI(openai_api_key= os.getenv("Open_API_KEY"),model_name = "text-davinci-003",temperature= 0.4)
    response=llm(question)
    return response
    
########## st

st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
#response = get_openai_response(input)

#get_openai_response(input)
submit = st.button("####################--------ask Q-----------##############")

if input:
    response = get_openai_response(input)
    st.subheader("The response is ")
    st.write(response)