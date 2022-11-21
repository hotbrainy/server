

from flask import request


def send_email_verification(mail, to):
    subject = "Confirm your email address"
    template = 'Error. [[[button_link]]]'
    """
    *****************************************************
    """
    try:
        with open("example.html","r",encoding="utf8") as w:
            template = w.read()
    except: pass
    button_url = request.host_url + "confirm-email/" + "123123213123123213"
    template = template.replace("[[[button_link]]]", button_url)
 
    msg = Message(
        subject,
        recipients=[to],
        html=template
    )
    assert msg.sender == "Me <me@example.com>"
    mail.send(msg)
