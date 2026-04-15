# ui.py
# This is the Streamlit UI for the NL2SQL application. It provides a simple interface for users to input their natural language questions, view the generated SQL queries, and see the results from the database. The UI also includes error handling and basic visualizations for numeric data. 

# Purpose: User interface and interaction layer for application. 
# It allows users to ask questions in natural language, sends those questions to the backend API, and displays the generated SQL and query results in a user-friendly format. 
# The UI also maintains a chat history for better user experience.


import streamlit as st
import requests
import pandas as pd

# Set page config for better layout and title 
st.set_page_config(page_title="NL2SQL AI", layout="wide")

st.markdown("""
<style>
.chat-user {
    background-color: #DCF8C6;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
    text-align: right;
}
.chat-bot {
    background-color: #F1F0F0;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)


# sidebar for app title and instructions
st.sidebar.title("NL2SQL AI")
st.sidebar.markdown("Ask questions in plain English")

if "history" not in st.session_state:
    st.session_state.history = []

# Clear chat
if st.sidebar.button("Clear Chat"):
    st.session_state.history = [] # stores chat history


# main chat interface
st.title("NL2SQL Assistant")

# input box for user to ask questions
question = st.text_input("Ask your question:")

if st.button("Run Query"):
    if question:
        with st.spinner("Generating SQL & fetching data... "):
            try:
                # sends question to backend API and gets response with sql and results or error msg.
                response = requests.post(
                    "http://127.0.0.1:8000/query",
                    json={"question": question},
                    timeout=5 # set timeout to avoid hanging if backend isn't running 
                )

                data = response.json()

            except requests.exceptions.ConnectionError:
                st.error("Backend not running.\n\nRun: uvicorn main:app --reload")
                data = {"error": "Backend not running"}

            except Exception as e:
                st.error(f"Unexpected error: {e}")
                data = {"error": str(e)}

            st.session_state.history.append({
                "question": question,
                "response": data
            })


# display chat history in reverse order with question on right and response on left.
for item in reversed(st.session_state.history):

    # USER MESSAGE
    st.markdown(f'<div class="chat-user"> {item["question"]}</div>', unsafe_allow_html=True)

    data = item["response"]

    # BOT MESSAGE 
    with st.container():
        st.markdown('<div class="chat-bot"> Response</div>', unsafe_allow_html=True)

        # Show SQL
        if "sql" in data:
            st.markdown("** Generated SQL:**")
            st.code(data["sql"], language="sql")

        # Show Results SAFELY
        if "result" in data and isinstance(data["result"], list):
            df = pd.DataFrame(data["result"])

            if not df.empty:
                st.markdown("**Results:**")
                st.dataframe(df, use_container_width=True)

                # Visualization for numeric columns if any exists
                numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

                if len(numeric_cols) >= 1:
                    st.markdown("**Visualization:**")
                    st.bar_chart(df[numeric_cols])
            else:
                st.info("No data found.")

        # Show Errors
        if "error" in data:
            st.error(data["error"])

    st.markdown("---")


# footer with project info
st.markdown("Built with FastAPI + Gemini + Streamlit")