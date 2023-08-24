# Put your app in here.
from flask import Flask, request
app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = a + b
    return str(result)

@app.route('/sub')
def subtract():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = a - b
    return str(result)

@app.route('/mult')
def multiply():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    result = a * b
    return str(result)

@app.route('/div')
def divide():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 1)) 
    result = a / b
    return str(result)

@app.route('/math')
def doMath():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    operation = request.args.get('op', 'add')

    if operation == 'add':
        result = a + b
    elif operation == 'sub':
        result = a - b
    elif operation == 'mult':
        result = a * b
    elif operation == 'div':
        result = a / b
    else:
        return "Invalid operation"

    return str(result)

if __name__ == "__main__":
    app.run()