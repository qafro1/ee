#This app will display Hello world that uses Flask, a small HTTP server for Python.
# Import the Flask class.
from flask import Flask

# Create an instance of this class
app = Flask(__name__)

# route() decorator to tell Flask what URL should trigger the function,and returns the message.
@app.route("/")

# Define the hello world function.
def hello():
    return "Hello World...*"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
