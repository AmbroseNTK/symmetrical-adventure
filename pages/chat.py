import streamlit as st
from model import Gemini
import google.generativeai as genai

def initialize_session_state():
    return st.session_state.setdefault("messages", [])

def get_generation_config_from_sidebar():
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.9, 0.1)
    top_p = st.sidebar.number_input("Top P", 0.0, 1.0, 1.0, 0.1)
    top_k = st.sidebar.number_input("Top K", 1, 100, 1)
    max_output_tokens = st.sidebar.number_input("Max Output Tokens", 1, 10000, 2048)

    return {
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "max_output_tokens": max_output_tokens,
    }

def handle_user_input(api_key, model):
    prompt = st.chat_input("Ask me anything!")
    if not prompt:
        st.error("Please enter a message to continue.")
        st.stop()

    try:
        st.session_state.messages.append({"role": "user", "parts": prompt})
        st.chat_message("user").write(prompt)
        
        genai.configure(api_key=api_key)
        gemini = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                        generation_config=model.generation_config,
                                        safety_settings=model.safety_settings)
        
        response = gemini.generate_content([prompt])
        
        if response.text:
            st.session_state.messages.append({"role": "assistant", "parts": response})
            st.chat_message("assistant").write(response.text)
        else:
            st.chat_message("assistant").write("I'm sorry, I don't understand.")
    except Exception as e:
        st.write(f"An error occurred: {str(e)}")


def prompt():
    st.title("💬 Chat2Query")
    st.caption("🚀 A streamlit chatbot powered by Sundar LLM")

    initialize_session_state()
    messages = st.session_state.messages

    if not messages:
        messages.append({
            "role": "assistant",
            "parts": "Hello, I'm a chatbot. Ask me anything!"
        })

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["parts"])

    gemini_key = st.text_input("Enter your Gemini API Key", key="chatbot_api_key", type="password")

    if not gemini_key:
        st.info("Please add your Gemini API key to continue.")
        st.stop()
    else:
        st.success("API key added successfully.")

    generation_config = get_generation_config_from_sidebar()
    my_model = Gemini("gemini-1.0-pro", generation_config, Gemini.get_safety_settings())

    handle_user_input(gemini_key, my_model)

    