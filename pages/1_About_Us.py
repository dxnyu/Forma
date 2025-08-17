import streamlit as st
from helper_functions.utility import check_password

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.title("About Us")

st.subheader("Project Scope")
st.write("""
Build a web tool that helps businesses get more information about setting up a business in Singapore and programs that are relevant for them.
""")

st.divider()

st.subheader("Objectives")
st.write("""
Forma serves as a business advisor that:
        \n1. Addresses queries on setting up a business in Singapore, including on procedure and regulations
        \n2. Based on user input on type of industry or business activity, find relevant government programs that could be of interest to the company
        \n3. Provide details to queries on EDB's incentives and programs.
""")

st.divider()

st.subheader("Data Sources")
st.write("""
- Singapore Government websites
- EDB Incentives and Facilitation factsheets (as found on https://www.edb.gov.sg/en/incentives-and-programmes/incentives-and-facilitation-programmes.html)
        """)

st.divider()

st.subheader("Features")
st.write("""
1. Set Up Your Business in Singapore: ChatBot that responds to user queries based on LLM generated responses\n
2. Find Government Support: CrewAI flow to respond to user queries\n
3. Explore EDB Incentives and Facilitation: RAG based on EDB incentive and facilitation factsheets to respond to user queries
        """)