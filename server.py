"""This module contains the server code for the mathematics problem solver."""

from flask import Flask, render_template, request
from flask_cors import CORS
from Maths.mathematics import (
    summation,
    subtraction,
    multiplication,
    division,
    power,
    modulus,
    integer_division,
    pythagoras,
    )

app = Flask("Mathematics Problem Solver")
CORS(app)
@app.route("/sum", methods=["GET"])
def sum_route():
    """This function returns the sum of two numbers."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = summation(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400

@app.route("/sub")
def sub_route():
    """This function returns the difference between two numbers."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = subtraction(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400

@app.route("/mul")
def mul_route():
    """This function returns the product of two numbers."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = multiplication(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400

@app.route("/div")
def div_route():
    """This function returns the division of two numbers."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        if num2 == 0:
            return {'result': "Invalid input. Cannot divide by zero."}, 400
        result = division(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400
    except ZeroDivisionError:
        return {'result': "Invalid input. Cannot divide by zero."}, 400

@app.route("/pow")
def pow_route():
    """This function returns the power of a number."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = power(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400

@app.route("/mod")
def mod_route():
    """This function returns the modulus of two numbers."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        if num2 == 0:
            return {'result': "Invalid input. Cannot divide by zero."}, 400
        result = modulus(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400
    except ZeroDivisionError:
        return {'result': "Invalid input. Cannot divide by zero."}, 400

@app.route("/intdiv")
def intdiv_route():
    """This function returns the integer division of two numbers."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        if num2 == 0:
            return {'result': "Invalid input. Cannot divide by zero."}, 400
        result = integer_division(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400
    except ZeroDivisionError:
        return {'result': "Invalid input. Cannot divide by zero."}, 400

@app.route("/pythag")
def pythag_route():
    """This function returns the hypotenuse of a right-angled triangle."""
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        result = pythagoras(num1, num2)
        return {'result':str(result)}, 200
    except ValueError:
        return {'result': "Invalid input. Please provide two numbers."}, 400

@app.route("/")
def render_index_page():
    """This function renders the index page."""
    return render_template('index.html')

@app.route("/hello")
def hello():
    """This function returns a greeting message."""
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
