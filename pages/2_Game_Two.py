import streamlit as st
import pandas as pd
from groq import Groq

client = Groq(api_key="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")

##########################################################################################################################################################################################

st.title("Selection Game")
st.audio("Gaming_Music.mp3", format="audio/mp3", autoplay=True, loop=True)

def generate_response(prompt):
    userPrompt = {
        "role": "user",
        "content": prompt
    }
    messageLog = [userPrompt]
    try:
        chat_completion = client.chat.completions.create(
            messages=messageLog,
            model="llama3-70b-8192",
            temperature=0.5
        )
        # Extract and return the content of the first choice
        return chat_completion.choices[0].message["content"].strip()
    except Exception as e:
        # Print the exception for debugging purposes
        print(f"Error: {e}")
        # Handle errors and return "N/A" if an exception occurs
        return "N/A"

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
    st.write(response)
