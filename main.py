import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"

template = """
    Below is an email that may be poorly worded. 
    Your goal is to:
    -Properly format the email
    -Convert the input text to a specified tone
    -Convert the input text to fit the specified word range

    Here are some examples of different tones:
    - Formal: I went to Italy this past weekend. I have numerous things to tell you about.
    - Friendly: I was just in Italy this past weekend. Had a great time, I have lots to tell you.

    The length of the email should be set to the length specified. If the length is 0-50 words, the 
    email you write should be 0 to 50 words long. If the length is 50+ words, the email you write 
    should be 50 or more words long. 
    
    Below is the email, tone, and length:
    TONE: {tone}
    LENGTH: {length}
    EMAIL: {email}

    YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables={"tone", "length", "email"},
    template=template,
)

def load_LLM():
    """Logic for loading the chain should go here"""
    llm=OpenAI(temperature=0.5)
    return llm

llm=load_LLM()
st.set_page_config(page_title="Globalize Email", page_icon="robot: ")
st.header("Globalize Text")


st.markdown("Often, professionals would like to improve the quality of their emails, but don't have the \
            skills to do so - I created a tool to help with this problem. Simply input the gist of your \
            email and select your preferred style from the dropdown menus, and an enhanced, professional \
            version of your email will be outputted. Built by Joey Johnson using OpenAI, Langchain and Streamlit.")

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        "What sort of tone would you like your email to have?",
        ('Formal', 'Friendly')
    )
with col2:
    option_length = st.selectbox(
        "How long should the email be?",
        ('0-50 words', '50+ words')
    )

def get_text():
    input_text = st.text_area(label="", placeholder="Tell Jerry Smith that I have to postpone our Friday meeting", key="email_input")
    return input_text

email_input = get_text()

st.markdown("### Your Converted Email:")

if email_input:
    prompt_email = prompt.format(tone=option_tone, length=option_length, email=email_input)
    formatted_email = llm(prompt_email)
    st.write(formatted_email)

