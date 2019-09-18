import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def notify(email_to):

    message = Mail(
        from_email='no-reply@iconicious.pythonanywhere.com',
        to_emails=email_to,
        subject='Hi, lets go to iconicious.pythonanywhere.com to play',
        html_content='<strong>Winter is coming</strong>')
    try:
        sg = SendGridAPIClient('KEY')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))
