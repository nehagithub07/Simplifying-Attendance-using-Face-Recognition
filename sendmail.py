import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendingEmail(table): 
    sender_email = "teamvisions22@gmail.com"
    receiver_email = "nehasaniya465@gmail.com"
    password = ""


    msg = MIMEMultipart("alternative") 
    msg['From'] = sender_email
    msg['To'] = receiver_email 

    msg['Subject'] = "Attendence List"
    html = f"{table}"

    part = MIMEText(html, "html")
    msg.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, msg.as_string()
        )
        server.quit()
