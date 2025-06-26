#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install langchain


# In[2]:


#!pip install streamlit


# In[3]:


#!pip install openai

# In[4]

#!pip install langchain-google-genai

# In[5]:
import streamlit as st

st.set_page_config(page_title="🦜🔗 뭐든지 질문하세요~ ")
st.title('🦜🔗 뭐든지 질문하세요~ ')

from langchain_google_genai import ChatGoogleGenerativeAI
import os
os.environ["GOOGLE_API_KEY"] = ''

def generate_response(input_text):  #llm이 답변 생성
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
        # other params...
    )

    st.info(llm.invoke(input_text))

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?') #첫 페이지가 실행될 때 보여줄 질문
    submitted = st.form_submit_button('보내기')
    generate_response(text)







