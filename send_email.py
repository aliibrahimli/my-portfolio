import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

receiver = "alibrahimli041@gmail.com"
username = "alibrahimli041@gmail.com"
password = "pckxbssmffhdbebb"

context = ssl.create_default_context()

message = """\
Subject: Hi! 
How are you?
Bye 
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)