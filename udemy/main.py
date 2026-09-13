from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask application</h1></html>" 

@app.route("/index ")
def index():
    return "This is a index page to showcase the backend turn."

if __name__ == "__main__":
    app.run(debug = True)