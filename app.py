# imports Flask which will be used as the web server, imports what we need
# also imports Math for the exponent operation
from flask import Flask, render_template, request
import math

# Declares the my_calculator app
app = Flask(__name__)

# Starts the route for the app
@app.route('/')

# defines the main function
def main():
    return render_template('app.html')


# defines the send function to process the request
@app.route('/send', methods=['POST'])
def send(sum=sum):
    # if a request is received the following code executes
    if request.method == 'POST':
        # grabs the numbers from the HTML template and saves into local variables
        # so we can perform operations on them in Python
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        # checks the value of operation to see what "Spell" to perform
        # all operations will use the variable 'sum' for simplicity
        # but the actual operations saved into sum are different
        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum="The wizard flicks his wand and numbers begin to float in the air.... "
                                                   + str(sum) + " !")

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum="The wizard flicks his wand and numbers begin to float in the air.... "
                                                   + str(sum) + " !")

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum="The wizard flicks his wand and numbers begin to float in the air.... "
                                                   + str(sum) + " !")

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum="The wizard flicks his wand and numbers begin to float in the air.... "
                                                   + str(sum) + " !")

        elif operation == 'exponent':
            sum = math.pow(float(num1), float(num2))
            return render_template('app.html', sum="The wizard flicks his wand and numbers begin to float in the air.... "
                                                   + str(sum) + " !")

        # Otherwise, no operation is POSTed
        else:
            return render_template('app.html')


# this runs the app in debug mode in the terminal, but does not affect the output the user sees
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
