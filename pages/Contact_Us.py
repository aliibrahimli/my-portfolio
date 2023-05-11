import re

import streamlit as st
import send_email

st.header("Contact Me")

with st.form(key="email_formss"):
    user_email = st.text_input("Your email address: ", placeholder="Write your email address here...")
    message1 = st.text_area("Your message here: ", placeholder="Write your message here...")
    message1 = message1 + "\n" + user_email


    button = st.form_submit_button("Submit")
    if button:
        if not user_email or not message1:
            if not user_email:
                st.error('Please write your email address before submitting.')
            if not message1:
                st.error('Please write text before submitting.')
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
            st.error('Please enter a valid email address.')
        else:
            st.success('Message sent.')
            send_email.send_email(message1)