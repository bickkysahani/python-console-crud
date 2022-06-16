import smtplib,os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

your_email = os.getenv('YOUR_EMAIL_ADDRESS')
app_password = os.getenv('APP_PASSWORD')

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to  
    user = your_email  #your email address
    msg['from'] = user  #your app password, generated from google account
    password = app_password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg) # <- UPDATED
    server.quit()

# email_alert("hey", "Hello world","bickky@gmail.com")