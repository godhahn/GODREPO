import streamlit as st
import pandas as pd
from groq import Groq

client = Groq(api_key = "")
dataset = pd.read_csv("Game_One_Dataset.csv")

##########################################################################################################################################################################################

def get_nature(description):
    userPrompt = {
        "role": "user",
        "content": f"Given the following description: {description}, identify if the description is positive or negative. Return only string Negative or string Positive as the answer. Give answer WITHOUT any explanation."
    }
    messageLog = [userPrompt]
    try:
        chat_completion = client.chat.completions.create(messages = messageLog, model = "llama3-70b-8192", temperature = 0.5)
    except:
        return ["N/A"]
    return chat_completion.choices[0].message.content

##########################################################################################################################################################################################

st.title("Description Game")
st.audio("Gaming_Music.mp3", format = "mp3", autoplay = True, loop = True)

name = st.text_input("Enter Your Name:")

if name:
    st.write(f"Hello {name}!")
    st.write("Let's play a Description Game!")
    
description = st.text_input("Describe Yi Hahn in One Sentence:")

if description:
    nature = get_nature(description)

    if nature == "Negative":
        negative_comments = dataset.loc[dataset["Nature"] == "Negative", "Description"]
        random_comment = negative_comments.sample().values[0]
        st.write(random_comment)
        st.write("Try again!")
    elif nature == "Positive":
        positive_comments = dataset.loc[dataset["Nature"] == "Positive", "Description"]
        random_comment = positive_comments.sample().values[0]
        st.write(random_comment)
        st.write("Applause!")

##########################################################################################################################################################################################