from distutils.log import error
from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


@app.route('/', methods=['POST', 'GET']) 
def index():
    try:
        number_1 = float(request.form.get("first"))
        number_2 = float(request.form.get('second'))
        operation = request.form.get('operation')

        result = requests.get(f"http://{operation}-service:5050/{number_1}/{number_2}")

        number_1=int(number_1) if number_1.is_integer() else number_1
        number_2=int(number_2) if number_2.is_integer() else number_2
        result = result.text

        def isfloat(num):
            try:
                float(num)
                return True
            except ValueError:
                return False

        if isfloat(result):
            result = round(float(result),2)
            if result.is_integer():
                result = int(result)

        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    except :
        flash("Please enter valid arguments")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
