import smtplib, ssl
import yaml


with open('config.yaml') as config_file:
        config = yaml.full_load(config_file)['data']

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ld.app.testing@gmail.com"  # Enter your address
receiver_email = "loic.diridollou@gmail.com"  # Enter receiver address
password = config["password"]
message = """\
Subject: Bike Service Notification

This is the state of the near-by station of 199 New Montgomery St."""

def email_sender():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
