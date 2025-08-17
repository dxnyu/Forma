import streamlit as st
from helper_functions.utility import check_password

if not check_password():  
    st.stop()

st.title("Methodology")
st.write("The flowcharts below represent how the LLM generates responses in each feature")

st.subheader("Set Up Your Business in Singapore")
st.image("./Flowcharts/Set Up Your Business in Singapore.jpg")

st.subheader("Find Government Support")
st.image("./Flowcharts/Find Government Support.jpg")

st.subheader("Explore EDB Incentives and Facilitation")
st.image("./Flowcharts/Explore EDB incentives and facilitation.jpg")
