#from experiments.email_test import email_sender
import os


if __name__ == "__main__":
    #email_sender()
    print(os.environ.get('EMAIL_PASSWORD'))
