from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/easter-eggs')
def easter():
    return 'Wow you found me'

@app.route('/1337')
def mastah():
    return 'i am l33t'
