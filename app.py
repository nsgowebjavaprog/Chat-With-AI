import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Ollama"

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, llm, temperature, max_tokens):
    ollama_model = Ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | ollama_model | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Title of the app
st.title("Talk With NS LONI Like A --[Chat-Bot]")

# Set the background image using CSS
background_style = """
<style>
.stApp {
    background-image: url('https://media.licdn.com/dms/image/D5612AQG3SfgIUWCdlg/article-cover_image-shrink_600_2000/0/1718768190769?e=2147483647&v=beta&t=Dzpw1AS6Iu14O8IyhFG6zk2ykdRSn_ReZpfn-w0ULOY');
    background-size: cover;
}
</style>
"""
st.markdown(background_style, unsafe_allow_html=True)

# Function to change the sidebar color
def change_sidebar_color(color):
    sidebar_bg = f"""
    <style>
    [data-testid="stSidebar"] {{
        background-color: rgb(60, 59, 58);
    }}
    </style>
    """
    st.markdown(sidebar_bg, unsafe_allow_html=True)

# Change the sidebar background color to red
change_sidebar_color("#FF0000")

# Select the OpenAI model
llm = st.sidebar.selectbox("Select Open Source model", ["llama3.2", "gemma2", "llama3.1", "gemma2:2b"])

# Adjust response parameters
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# Main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write(response)
else:
    st.write("Provide the user input")

# Footer implementation
footer_html = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgb(60, 59, 58);
    color: white;
    text-align: center;
    padding: 10px;
}
</style>

<div class="footer">
    <p>Developed with NS ❤️ LONI <a style='display: block; text-align: center; backgroug-color:rgb(60, 59, 58)' href="https://www.example.com" target="_blank">Nagaraj Loni</a></p>
    </div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
