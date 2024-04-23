import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Set up SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    server.send_message(msg)
    del msg  # Delete the message object to release resources
    server.quit()

def main():
    # Load Excel workbook
    wb = openpyxl.load_workbook('Book1.xlsx');  # Replace 'example.xlsx' with your Excel file path
    ws = wb.active
    msg = 'Dear Participants please join the GCR by using following link \n https://www.youtube.com/watch?v=43e8dPUt7RY&list=RDQI0SxKT388M&index=2&ab_channel=SRMusicOfficial'

    # Iterate through email addresses in column E
    for cell in ws['E']:
        recipient_email = cell.value
        if recipient_email:
            # Replace sender_email and sender_password with your Gmail credentials
            send_email('', '', recipient_email, 'Speed Programming GCR', msg)

if _name_ == "_main_":
    main()