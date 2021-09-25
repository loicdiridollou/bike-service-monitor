"""Elements to send the email"""
import os
import ssl
import smtplib
import yaml


if not os.environ.get("EMAIL_PASSWORD"):
    with open('config/local_config.yaml', 'rb') as config_file:
        config = yaml.full_load(config_file)['data']
        os.environ.update(config)



def email_sender(message, test_mode=False):
    """Function to send email"""
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "ld.app.testing@gmail.com"
    receiver_email = "loic.diridollou@gmail.com"
    password = os.environ.get("EMAIL_PASSWORD")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        if not test_mode:
            server.sendmail(sender_email, receiver_email, message)
