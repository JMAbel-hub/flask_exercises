# Worked with Joe Onghena 
from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    number = request.args.get('number')
    # if the input is not empty
    if(number != ''):
        # safely tests if the input is a number
        try:
            int(number)
            isNumber = True
        except ValueError:
            isNumber = False

        # in the case the input is a number
        if isNumber:
            # even case
            if float(number) % 2 == 0:
                number = str(number) + " is even"
            # odd case
            else:
                number = str(number) + " is odd"
        # in the case the input is not an integer
        else:
            number = str(number) + " is not an integer!"
    else:
        number = "No number provided!"
    return render_template('calculate.html', number = number)
