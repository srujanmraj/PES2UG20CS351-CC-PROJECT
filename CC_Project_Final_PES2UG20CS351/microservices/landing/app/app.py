from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


# def add(n1, n2):
#     return n1+n2

# def minus(n1, n2):
#     return n1-n2

# def multiply(n1, n2):
#     return n1*n2

# def divide(n1, n2):
#     return n1/n2

@app.route('/', methods=['POST', 'GET'])
def index():
    try :
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
        operation = request.form.get('operation')
    except : 
        number_1 : 0
        number_2 : 0
        operation = 'null'
    else:
        result = 0
        if operation == 'add':
            result = requests.get("http://addition:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'minus':
            result = requests.get("http://subtraction:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'multiply':
            result = requests.get("http://multiplication:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'divide':
            result = requests.get("http://division:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'gcd':
            result = requests.get("http://gcd:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'lcm':
            result = requests.get("http://lcm:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'modulus':
            result = requests.get("http://modulus:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'exponent':
            result = requests.get("http://exponent:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'gt_than':
            result = requests.get("http://gtthan:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'ls_than':
            result = requests.get("http://lsthan:5050/"+str(number_1)+"/"+str(number_2)).text
        elif operation == 'equal':
            result = requests.get("http://equal:5050/"+str(number_1)+"/"+str(number_2)).text
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )