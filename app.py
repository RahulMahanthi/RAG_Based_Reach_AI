import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom CSS styling for a sleek, modern UI
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Arial', sans-serif;
        }
        .main {
            background: #181818;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.1);
        }
        .stTextInput textarea, .stChatInput input {
            color: #fff !important;
            background: #252525 !important;
            border-radius: 8px;
            padding: 10px;
        }
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
            margin: 5px 0;
        }
        .stChatMessage[data-role="user"] {
            background: #37474F;
        }
        .stChatMessage[data-role="ai"] {
            background: #263238;
        }
        .sidebar .sidebar-content {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 CodeGenius AI")
st.caption("🚀 Your Real-Time AI Coding Assistant")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )
    st.markdown("---")
    st.markdown("**✨ Features:**")
    st.markdown("✔️ Code Debugging")
    st.markdown("✔️ Solution Design")
    st.markdown("✔️ Python & More")
    st.markdown("✔️ AI-Powered Assistance")
    st.markdown("---")
    st.markdown("💡 Built with [Ollama](https://ollama.ai/) & [LangChain](https://python.langchain.com/)")

# Initialize the chat engine
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are CodeGenius AI, a highly intelligent coding assistant. Provide clear, optimized solutions in Python and other languages. Keep responses concise and professional."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hello! I'm CodeGenius AI. How can I assist you today? 💡"}]

# Chat UI with real-time updates
chat_container = st.container()
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Function to process AI response
def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

# Function to construct the prompt chain
def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

# User input and AI response processing
user_query = st.chat_input("Ask me anything about coding...")
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})
    with st.spinner("🤖 Thinking..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    st.rerun()
