import pandas as pd
import os
import ssl
import smtplib
from email.message import EmailMessage
import easygui as eg

path = eg.fileopenbox()
emails_df = pd.read_csv(path)
emails = emails_df['email']
names = emails_df['name']
email_sender = "" #sender email

email_password = "" #sender email pass key ( App Password )
subject = ''
count = 0
total_emails = len(emails)
for  data in zip(emails, names):
    body = f''' '''

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = data[0]
        em['Subject'] = subject
        em.set_content(body)
        
        try:
            smtp.send_message(em)
            count += 1
            print("[+]:  ", data[0])
        except Exception as e:
            print("[-]  Error: ", e)

# print(count)
if(count == total_emails):
    print("[+]  Emails sent successfully.")
  