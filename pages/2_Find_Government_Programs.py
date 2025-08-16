__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# From public libraries
import streamlit as st
import openai 
import markdown
from bs4 import BeautifulSoup

# From my scripts
from helper_functions import llm
from logics import user_query_handler1

st.title('Find out about incentives and programs offered by the Singapore Government.\n')

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Share about your company and business interests here:", height=150)

if form.form_submit_button("Submit"):
    # Get user input
    st.toast(f"User Input Submitted - {user_prompt}")

    # Generate response
    response = user_query_handler1.crew.kickoff(inputs={"question": user_prompt})
    
    st.write(response.raw)
    print(f"User Input is {user_prompt}")
