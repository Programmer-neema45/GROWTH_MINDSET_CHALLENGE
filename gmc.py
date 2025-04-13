import streamlit as st
import random

challenges = [
    "Try something new today!",
    "Learn from a mistake.",
    "Ask for feedback.",
    "Do one thing that scares you.",
    "Practice something you're not good at."
]

quotes = [
    "Mistakes are proof that you're trying.",
    "You can learn anything with effort.",
    "Not yet is better than not ever.",
    "Every challenge is a chance to grow.",
    "Keep going, you're improving!"
]

st.title("🌱 Growth Mindset Challenge")

if st.button("new Challenge"):
    st.session_state.challenge = random.choice(challenges)
    st.session_state.quote = random.choice(quotes)

# Show saved or initial values
challenge = st.session_state.get("challenge", random.choice(challenges))
quote = st.session_state.get("quote", random.choice(quotes))

st.subheader("🧠 Today's Challenge")
st.write(challenge)

st.subheader("💬 Motivation")
st.write(f"_{quote}_")
