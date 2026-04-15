import streamlit as st
from llm import convert_to_sql
from db import run_sql

st.title("Text to SQL Chat")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
query = st.chat_input("Ask your question")

if query:

    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    # Convert to SQL
    sql = convert_to_sql(query)

    try:
        result = run_sql(sql)

        response = f"""
Generated SQL:
{sql}

Result:
{result}
"""

    except Exception as e:
        response = f"Error: {str(e)}"

    # Add assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])