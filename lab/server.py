# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return {"message":"hello world"}

@app.route("/no_content")
def no_content():
    # Send custom HTTP code back with a tuple
    return ("No content found", 204)