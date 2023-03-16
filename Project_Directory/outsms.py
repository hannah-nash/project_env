from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from num2words import num2words

app = Flask(__name__)

account_sid = 'ACea7d5b4cf2b9baa11d66908ea1c9d2e8'
auth_token = 'fb9024cbe96e46c9282b43fdada034ee'
twilio_phone_number = '18886174718'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="This is my test message.",
                    from_='+18886174718',
                    to='+14258024796'
                )
print(message.sid)
