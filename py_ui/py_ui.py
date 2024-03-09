from flask import Flask, request, jsonify
from flask_cors import CORS
from config import CONFIG
from utils import engine as Engine
from components.button import Button
from components.view import View
from components.text import Text
from components.image import Image
from components.page import Page
from utils.styles import createStyles, useStyles

# the main layer to orchestrate everything
app = Flask(__name__)
CORS(app)


@app.before_request
def handleIncoming():
    # preprocess request payload
    pass


@app.route('/', methods=['GET'])
def renderApp():
    payload = request.get_json()
    # do some stuff with payload

    response = "Hello world!"
    return jsonify(response)


@app.after_request
def handleOutGoing():
    # post process response
    pass


if __name__ == '__main__':
    app.run(CONFIG['host'], CONFIG['port'], CONFIG['debug'], CONFIG['thread'])
