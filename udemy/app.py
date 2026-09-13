from flask import Flask
'''
It creates an instance of the Flask class,
which will be your WSGI (web server gateway interface ) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask application! This should be an amazing experience for you. We will try to make it as simple as possible for everyone.Thank you for visiting us."

@app.route("/index")
def index():
    return "This is a index page to show case the backend turn."

if __name__ == "__main__":
    app.run(debug = True)
