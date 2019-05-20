from flask import Flask, request, make_response
from Service import Auth, InputValidation, Models
from Utils import api_utils
import json
import random
import base64, os

app = Flask(__name__)
app.config.from_object('config.BaseConfig')

@app.route('/', methods=['POST'])
def index():
    """
    Main Api
    """
    authValue = request.headers.get('Authorization')
    if Auth.auth(authValue):
        response = {
                'errorCode': 222,
                '_id': '',
                'xpressId': '',
                'taskId': '',
                'error': ''
        }
        try:
              verificationInput = request.json
        except:
                response['error'] = 'Not a Valid input'
                return response
        verificationResponse = InputValidation.verification_input(verificationInput)
        if verificationResponse is not None:
                response['error'] = verificationResponse
                return json.dumps(response)
        else:
                verificationOutput = api_utils.get_verification(verificationInput)
                return verificationOutput
    else:
            return make_response("UnAuthorize User", 401)

