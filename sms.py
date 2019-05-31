# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC270f7b9db6fd4ffe69fdf521ff2a079f'
auth_token = '9294a9632573f35079d48eaa116e393c'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13058766513',
                     to='+17863806908'
                 )

print(message.sid)