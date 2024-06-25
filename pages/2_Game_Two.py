import streamlit as st
import pandas as pd
from groq import Groq

client = Groq(api_key = "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")

##########################################################################################################################################################################################

st.title("Selection Game")
st.audio("Gaming_Music.mp3", format = "mp3", autoplay = True, loop = True)

# Function to generate response from GPT
def generate_response(prompt):
    response = client.chat.completions.create(model="llama3-70b-8192", messages=[prompt])
    return response.choices[0].text.strip()

# Options for the game
options = ["Option 1: Ask for a joke", "Option 2: Ask for a motivational quote", "Option 3: Ask for a random fact"]

# Display options and get user selection
selection = st.radio("Choose an option:", options)

# Generate prompt based on selection
if selection == options[0]:
    prompt = "Tell me a joke."
elif selection == options[1]:
    prompt = "Give me a motivational quote."
elif selection == options[2]:
    prompt = "Tell me a random fact."

# Button to generate response
if st.button("Get Response"):
    response = generate_response(prompt)
    if response.choices:
        st.write(response.choices[0].text.strip())
    else:
        st.write("No response generated.")
