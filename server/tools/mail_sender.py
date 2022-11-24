
import os

from flask import request


from flask_mail import Message, Mail
    
def send_email_verification(to, subject, template, mail):
    print(to)
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=os.getenv('MAIL_DEFAULT_SENDER')
    )
    mail.send(msg)
