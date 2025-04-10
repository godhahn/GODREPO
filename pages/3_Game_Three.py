import random
import streamlit as st

def soccer_game():
    st.title("Welcome to 'Soccer Penalty Shootout'!")
    st.write("Try to score a goal!")

    if 'user_score' not in st.session_state:
        st.session_state.user_score = 0
        st.session_state.computer_score = 0

    if 'round' not in st.session_state:
        st.session_state.round = 1

    st.write(f"Round {st.session_state.round}")

    user_choice = st.selectbox("Choose your shot direction:", ["Left", "Center", "Right"])
    if st.button("Shoot"):
        computer_choice = random.choice(["Left", "Center", "Right"])
        st.write(f"Goalkeeper dives to: {computer_choice}")

        if user_choice == computer_choice:
            st.write("Goalkeeper saves it! No goal.")
            st.session_state.computer_score += 1
        else:
            st.write("Goal!!!")
            st.session_state.user_score += 1

        st.session_state.round += 1

        st.write(f"Score: You {st.session_state.user_score} - {st.session_state.computer_score} Computer")

if __name__ == "__main__":
    soccer_game()

