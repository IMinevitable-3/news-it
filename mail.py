from email.message import EmailMessage
import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()
subject = "Email Subject"
body = "This is the body of the text message"
sender = os.environ.get("SENDER")
recipients = os.environ.get("RECIEVER")
password = os.environ.get("PASSWORD")


def send_email(subject, body, sender=sender, recipients=recipients, password=password):
    em = EmailMessage()
    print(sender, recipients)
    em["From"] = sender
    em["To"] = recipients
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recipients, em.as_string())


# Send the email
send_email(subject, body, sender, recipients, password)
