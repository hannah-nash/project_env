from flask import Flask, request, redirect
from num2words import num2words

app = Flask(__name__)

text_input = input("Enter amount of check in cents: ")


        
        # check if the message is a number
try:
    amount = int(text_input)
except ValueError:
    print("Please send a valid number.")
        
        # convert the number to words and cents
dollars = num2words(amount // 100)
length = len(text_input)
cents = text_input[length - 2:]
print("That value in words is: ", f"{dollars} and {cents}/100")

if __name__ == "__main__":

    app.run(debug=True)