"""Encapsulation of SES email notification."""
import boto3
from botocore.exceptions import ClientError

def send_email(recipients=[]):
    """Main encapsulation."""
    AWS_REGION = "us-west-1"
    client = boto3.client('ses', region_name=AWS_REGION)
    CHARSET = "UTF-8"
    SENDER = "ld-app-testing (AWS) <ld.app.testing@gmail.com>"

    message = "Hello my name is SES"

    SUBJECT = "Bike Service Notification"
    BODY_TEXT = (message)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses':
                    recipients,
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

    return {
        'statusCode': 200,
        'body': response
    }
