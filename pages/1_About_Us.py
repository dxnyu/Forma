import streamlit as st

st.title("About Us")

st.subheader("Project Scope")
st.text_area("""
Build a web tool that helps businesses get more information about setting up a business in Singapore and programs that are relevant for them.
""")

st.divider()

st.subheader("Objectives")
st.text_area("""
Forma serves as a business advisor that:
        1. Addresses queries on setting up a business in Singapore, including on procedure and regulations
        2. Based on user input on type of industry or business activity, find relevant government programs that could be of interest to the company
        3. Provide details to queries on EDB's incentives and programs.
""")

st.divider()

st.subheader("Data Sources")
st.text_area("""
- Singapore Government websites
- EDB Incentives and Facilitation factsheets (as found on https://www.edb.gov.sg/en/incentives-and-programmes/incentives-and-facilitation-programmes.html)
        """)

st.divider()

st.subheader("Features")
st.text_area("""
Search functions that gather relevant information for the user.
        """)