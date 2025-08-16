import streamlit as st
from helper_functions import llm

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

st.title("Ask me about setting up an entity in Singapore")

system_prompt = """
You are a Singapore government official working for an investment promotion agency. 
An executive from a company asks you the query within the delimiters.

The executive is unfamiliar with the process of setting up an entity in Singapore, and would like to get more information.

Consider the following about the query:
- What is the executive asking about, e.g. process or regulations?
- What type of information could be relevant for the executive?

Think step by step.

<prompt>
{prompt}
</prompt>

Respond with information that is most relevant to the query, substantiating each point with 3 bullet points.
Also offer useful websites and resources for reference.

"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How may I help?"):
    st.session_state.messages.append({"role":"user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        system_message = [{"role": "system", "content": system_prompt}]
        
        stream = llm.client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=system_message.extend([{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]),
            stream=True,
        )
    response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
            





