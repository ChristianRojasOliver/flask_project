# Import the Flask class from the flask module
from flask import Flask, make_response

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
    return ({"message": "No content found"}, 204)

@app.route("/exp")
def index_explicit():
    # Create a response object with the message "Hello World"
    resp = make_response({"message": "Hello World"})
    # Set the status code of the response to 200
    resp.status_code = 200
    # Return the response object
    return resp
