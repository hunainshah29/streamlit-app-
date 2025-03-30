import streamlit as st
import random

def get_challenge():
    challenges = [
        "Think of a time you failed at something. What did you learn from it?",
        "Try something new today that you've never done before.",
        "Give yourself positive feedback instead of negative self-talk.",
        "Ask someone for constructive feedback and reflect on it.",
        "Write down one thing you struggled with today and how you can improve.",
        "Abilities and intelligence can be developed through effort, learning, and perseverance."
       
    ]
    return random.choice(challenges)

st.title("Growth Mindset Challenge By HUNAIN SHAH")


st.write("A growth mindset is about embracing challenges, learning from mistakes, and persisting through difficulties. Take on a challenge today!")

if st.button("Get a Growth Mindset Challenge"):
    challenge = get_challenge()
    st.subheader("Your Challenge:")
    st.write(challenge)

st.text_area("Describe a challenge you are facing ? (Optional)", "Write about your  challenge you are facing here...")

st.write("Remember, growth comes from effort and learning! Keep going! ")
