from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from num2words import num2words

app = Flask(__name__)

account_sid = 'ACea7d5b4cf2b9baa11d66908ea1c9d2e8'
auth_token = 'fb9024cbe96e46c9282b43fdada034ee'
twilio_phone_number = '18886174718'
client = Client(account_sid, auth_token)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    # check if the message is incoming or outgoing
    if request.method == 'POST':
        # get the message body
        message_body = request.form['Body']
        
        # check if the message is a number
        try:
            amount = int(message_body)
        except ValueError:
            resp = MessagingResponse()
            resp.message("Please send a valid number.")
            return str(resp)
        
        # convert the number to words and cents
        dollars = num2words(amount // 100)
        cents = amount % 100
        resp = MessagingResponse()
        resp.message(f"${dollars} and {cents:02d}/100")
        return str(resp)
    else:
        # this is a GET request, so return a message prompting the user to text the number
        return "Please text the amount in cents (e.g., 1234 for $12.34)."
if __name__ == "__main__":
    app.run(debug=True)


