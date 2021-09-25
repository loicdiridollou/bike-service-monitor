import smtplib, ssl
import yaml
import os
from experiments.data_acq_test import get_results
from datetime import datetime

if not os.environ.get("EMAIL_PASSWORD"):
    with open('config/local_config.yaml') as config_file:
        config = yaml.full_load(config_file)['data']
        os.environ.update(config)


def email_sender():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "ld.app.testing@gmail.com"  # Enter your address
    receiver_email = "loic.diridollou@gmail.com"  # Enter receiver address
    password = os.environ.get("EMAIL_PASSWORD")
    message = """\
    Bike Service Notification

This is the state of the near-by station of 199 New Montgomery St.\n"""
    
    values = get_results()
    for elem in values:
        llist = [field + ': ' + str(elem[field]) for field in elem]
        message += " | ".join(llist)
        message += "\n"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
