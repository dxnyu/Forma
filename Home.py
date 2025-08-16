# This program aims to:
# 1. Address queries on setting up a business in Singapore, including on procedure and regulations.
# 2. Based on user input on type of industry or business activity, find relevant government programs that could be of interest to the company.

import streamlit as st
from helper_functions.utility import check_password

# Check if the password is correct.  
if not check_password():  
    st.stop()

st.title("About Forma")

st.image("https://media.istockphoto.com/id/2103894518/photo/business-partners-in-meeting.jpg?s=612x612&w=0&k=20&c=Yxhksr9gMqIhk7Og8slPhCgov9w5h9al3cFBse3VkHM=")

st.write("Forma is your personalized business assistant in Singapore. \n \
Forma can help you set up your business in Singapore, find incentives & grants, and suitable business partners. \n \
Try asking Forma questions you have.")

with st.expander ("See Disclaimer"):
    st.write('''
    IMPORTANT NOTICE: This web application is developed as a proof-of-concept prototype. \
    The information provided here is NOT intended for actual usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.\
    Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.\
    Always consult with qualified professionals for accurate and personalized advice.
    ''')