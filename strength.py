import streamlit as st
import re

def check_password_strength(password):
    strength = "Weak"
    score = 0
    
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    
    return strength

st.title("Password Strength Checker By Hunain Shah ")
password = st.text_input("Enter your password", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"Password Strength: **{strength}**")
    
    if strength in ["Weak", "Moderate"]:
        st.warning("Consider using a longer password with uppercase, lowercase, numbers, and special characters.")
