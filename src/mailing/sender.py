"""Elements to send the email"""
import os
import ssl
import smtplib
import yaml
import data.core as dc


if not os.environ.get("EMAIL_PASSWORD"):
    with open('config/local_config.yaml', 'rb') as config_file:
        config = yaml.full_load(config_file)['data']
        os.environ.update(config)



def email_sender(message=None, stations=None, test_mode=False):
    """Function to send email"""
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "ld.app.testing@gmail.com"
    receiver_email = "loic.diridollou@gmail.com"
    password = os.environ.get("EMAIL_PASSWORD")

    if not message:
        message = """Bike Service Notification

                  """
        message += "\n"
        message += "This is the state of the near-by station of 199 New Montgomery St.\n"
    
        values = dc.get_results(stations)
        for elem in values:
            llist = [field + ': ' + str(elem[field]) for field in elem]
            message += " | ".join(llist)
            message += "\n"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        if not test_mode:
            server.sendmail(sender_email, receiver_email, message)


if __name__ == "__main__":
    email_sender(stations=['25', '363', '445'])