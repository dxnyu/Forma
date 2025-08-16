import streamlit as st
from helper_functions import llm 

st.title("Ask me questions on setting up a business entity in Singapore.\n")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Ask your question here:", height=150)

if form.form_submit_button("Submit"):
    # Get user input
    st.toast(f"User Input Submitted - {user_prompt}")

    # Chain of thought prompting
    prompt_1 = f"""
    You are a Singapore government official working for an investment promotion agency. 
    An executive from a company asks you the query within the delimiters.

    The executive is unfamiliar with the process of setting up an entity in Singapore, and would like to get easy to understand step-by-step advice on how to do so.
    
    Consider the following about the query:
    - What is the executive asking about, e.g. process or regulations?
    - What type of information could b relevant for the executive?

    Think step by step.

    Respond with information that is most relevant to the query.

    <query>
    {user_prompt}
    <query>

    """

    response_1 = llm.get_completion(prompt_1)

    prompt_2 = f"""
    Organize the information provided into key steps. Provide your response numerically and with 3 bullet points for each step.

    <items>
    {response_1}
    <items>

    """

    response_2 = llm.get_completion(prompt_2)

    st.write(response_2)
    print(response_2)