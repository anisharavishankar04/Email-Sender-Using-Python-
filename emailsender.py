import ssl
import smtplib
from email.message import EmailMessage

email_sender = 'sendermain@gmail.com'
email_password = 'yourpassword'  

email_receiver = 'receivermail@gmail.com'

subject = "You are a squeaky toy"
body = "You are a squeaky toy, kiddo"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
