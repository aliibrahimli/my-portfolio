import smtplib
import ssl
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    receiver = "alibrahimli041@gmail.com"
    username = "alibrahimli041@gmail.com"
    password = "pckxbssmffhdbebb"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)





