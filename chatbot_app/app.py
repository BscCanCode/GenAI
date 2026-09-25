import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="allam-2-7b")


# -----------------------------
# Chat history
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        (
            "system",
            "You are a friendly assistant. "
            "Always respond in English only. "
            "Never respond in Arabic or any other language, "
            "even if the user uses another language."
        )
    ]


# -----------------------------
# UI
# -----------------------------

st.set_page_config(
    page_title="My GenAI Chatbot",
    page_icon="🤖"
)

st.title("🤖 My GenAI Chatbot")
st.write("Ask me anything!")
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        (
            "system",
            "You are a friendly assistant. "
            "Always respond in English only. "
            "Never respond in Arabic or any other language."
        )
    ]
    st.rerun()

# Show previous messages
for role, content in st.session_state.messages:

    if role == "system":
        continue

    with st.chat_message(role):
        st.write(content)


# -----------------------------
# User input
# -----------------------------

query = st.chat_input("Ask anything...")


if query:

    # Show user's message
    with st.chat_message("user"):
        st.write(query)

    # Add user message to history
    st.session_state.messages.append(
        ("user", query)
    )

    # Generate AI response
    response = ""

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        for chunk in llm.stream(st.session_state.messages):

            response += chunk.content

            response_placeholder.write(response)

    # Add AI response to history
    st.session_state.messages.append(
        ("assistant", response)
    )