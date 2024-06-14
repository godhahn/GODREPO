import streamlit as st
from groq import Groq

client = Groq(api_key = "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")

##########################################################################################

def get_hint(description):
    userPrompt = {
        "role": "user",
        "content": "Given the following description: "
        + description
        + "when the description is positive, give applause for the user. No need to provide a hint."
        + "when the description is negative, please provide a hint towards the positive description."
    }
    messageLog = [userPrompt]
    try:
        chat_completion = client.chat.completions.create(messages=messageLog, model="llama3-70b-8192", temperature=0.1)
    except:
        return ["N/A"]
    hint = chat_completion.choices[0].message.content
    return hint

##########################################################################################

st.title("Description Game")

name = st.text_input("Enter Your Name:")

if name:
    st.write(f"Hello {name}! I love you so much!")
    st.write("Let's play a Description Game!")

description = st.text_input("Describe Yi Hahn Pang in One Sentence:")

if description:
    hint = get_hint(description)
    st.write(hint)
