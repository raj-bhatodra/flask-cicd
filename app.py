from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Automatic Diploy')
    return 'Hello, Docker!'
