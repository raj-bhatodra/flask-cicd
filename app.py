from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! I'm Docker, a platform for developing, deploying, and running applications in a containerized environment."
