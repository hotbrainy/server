


from flask_mail import Message


def send_email_verification(to, mail):
    subject = "Confirm your email address"
    template = 'Error. [[[button_link]]]'
    """
    *****************************************************
    """
    try:
        with open("example.html","r",encoding="utf8") as w:
            template = w.read()
    except: pass


    global Message
    msg = Message(
        subject,
        recipients=[to],
        html=template
    )
    mail.send(msg)
