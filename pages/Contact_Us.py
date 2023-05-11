import streamlit as st
import re

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address: ", placeholder="Write your email address here...")
    message = st.text_area("Your message here: ", placeholder="Write your message here...")
    button = st.form_submit_button("Submit")

    if button:
        if not user_email or not message:
            if not user_email:
                st.error('Please write your email address before submitting.')
            if not message:
                st.error('Please write text before submitting.')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):

            st.error('Please enter a valid email address.')
        else:
            st.success('Message sent.')

