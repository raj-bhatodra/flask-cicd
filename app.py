from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Automatic Deploy')
    print('Hello! World')

hello_world() 
