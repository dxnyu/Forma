# From public libraries
import streamlit as st

from helper_functions import llm 

st.title('Find out about government programs offered by the Singapore Government here.')

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=150)

if form.form_submit_button("Submit"):
    # Get user input
    st.toast(f"User Input Submitted - {user_prompt}")

    prompt_1 = f"""
    You are a Singapore government official working for an investment promotion agency. An executive from a company asks you the questions within the delimiters.

    The company is a foreign company, and the executive is unfamiliar with Singapore.
    The executive would like to be motivated with reasons to come to Singapore, whether that be business opportunities, partnerships, or government programs in Singapore.
    
    Respond with relevant information on Singapore's offerings that could support the company to set up business activities or find partnerships in Singapore.
    The information should be specific with examples of programs, instead of providing broad strokes on Singapore's attractiveness for businesses.

    Think step by step.

    <company_query>
    {user_prompt}
    </company_query>

    """

    response_1 = llm.get_completion(prompt_1)

    prompt_2 = f"""
    Of the items suggested, elaborate on how they could be relevant for the company when setting up a business in Singapore. 
    
    Think step by step. Provide your response in 3 bullet points for each program.

    <items>
    {response_1}
    <items>

    """

    response_2 = llm.get_completion(prompt_2)

    st.write(response_2)
    print(response_2)