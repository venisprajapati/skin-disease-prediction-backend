"""
Project Name: YouTube Transcript Summarizer
YouTube Transcript Summarizer API
"""


from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/api/', methods=['GET'])
def respond():

    image_id = request.args.get("image_id", None)

    body = {}

    # Build Response
    data = {}
    data['message'] = "Success"
    data['id'] = image_id
    data['response'] = "Predicted Disease - X"

    body["data"] = data

    # Return the response in json format
    return buildResponse(body)


# Welcome message to our server
@app.route('/')
def index():

    body = {}
    body['message'] = "Success"
    body['data'] = "Welcome to Skin-Disease Prediction API."

    return buildResponse(body)


# Build Response
def buildResponse(body):

    response = jsonify(body)

    return response


if __name__ == '__main__':

    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, debug=True)

