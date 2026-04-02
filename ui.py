import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="NL2SQL AI", layout="wide")

# ---------------------------
# Custom Styling
# ---------------------------
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

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("🧠 NL2SQL AI")
st.sidebar.markdown("Ask questions in plain English")

if "history" not in st.session_state:
    st.session_state.history = []

# Clear chat
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.history = []

# ---------------------------
# Main UI
# ---------------------------
st.title("💬 NL2SQL Assistant")

question = st.text_input("Ask your question:")

if st.button("Run Query"):
    if question:
        with st.spinner("Generating SQL & fetching data... ⏳"):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/query",
                    json={"question": question},
                    timeout=5
                )

                data = response.json()

            except requests.exceptions.ConnectionError:
                st.error("❌ Backend not running.\n\nRun: uvicorn main:app --reload")
                data = {"error": "Backend not running"}

            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
                data = {"error": str(e)}

            st.session_state.history.append({
                "question": question,
                "response": data
            })

# ---------------------------
# Display Chat
# ---------------------------
for item in reversed(st.session_state.history):

    # USER MESSAGE
    st.markdown(f'<div class="chat-user">🧑 {item["question"]}</div>', unsafe_allow_html=True)

    data = item["response"]

    # BOT MESSAGE
    with st.container():
        st.markdown('<div class="chat-bot">🤖 Response</div>', unsafe_allow_html=True)

        # Show SQL
        if "sql" in data:
            st.markdown("**🧠 Generated SQL:**")
            st.code(data["sql"], language="sql")

        # Show Results SAFELY
        if "result" in data and isinstance(data["result"], list):
            df = pd.DataFrame(data["result"])

            if not df.empty:
                st.markdown("**📊 Results:**")
                st.dataframe(df, use_container_width=True)

                # Visualization
                numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

                if len(numeric_cols) >= 1:
                    st.markdown("**📈 Visualization:**")
                    st.bar_chart(df[numeric_cols])
            else:
                st.info("No data found.")

        # Show Errors
        if "error" in data:
            st.error(data["error"])

    st.markdown("---")

# ---------------------------
# Footer
# ---------------------------
st.markdown("🚀 Built with FastAPI + Gemini + Streamlit")