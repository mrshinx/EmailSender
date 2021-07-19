import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


def CreateMail():
    email['from'] = input('Your name:')
    email['to'] = input('Send to: ')
    email['subject'] = input('Subject: ')
    receiver = input('Name of receiver: ')

    # Open html file and read it as text
    html = Template(Path('index.html').read_text())
    # Substitute name variable and set the content as html format
    email.set_content(html.substitute(name=receiver), 'html')


def Login(username, password):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, password)


def Send(username, password):
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, password)
        smtp.send_message(email)


while True:
    try:
        username = input('Your email address: ')
        password = input('Your password: ')
        Login(username, password)
    except smtplib.SMTPAuthenticationError as err:
        print(
            'Cannot login, please try again. You might want to turn on "Less secure app access" if you are using gmail')
        continue
    else:
        print('Login successfully')
        email = EmailMessage()
        CreateMail()
        Send(username, password)
        print('Email sent')
        break
