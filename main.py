'''
This is the server module. Within this module we check incoming post Messages
based on their respective Paths. To tighten the security, Webex needs to provide a
signature, based on a Webhook Secret. The incoming Information is parsed here and then passed
to the Bot Controller
'''
from flask import Flask, request
import hashlib
import hmac
import json
import logging
from chat_bot import controller
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), 'config/.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
secret_key=str(os.getenv('HOOKSECRET'))

# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Starting the server
@app.route('/messages', methods=['POST'])
def handle_message():
    if request.method == 'POST':
        data_raw = request.data
        data_json=json.loads(data_raw)
        signature_from_webex=request.headers.get('X-Spark-Signature')
        hashed_by_module = hmac.new(secret_key.encode(), data_raw, hashlib.sha1).hexdigest()
                
        if signature_from_webex==hashed_by_module: 
            if data_json['data']['personEmail']!=str(os.getenv('BOTMAIL')):
                controller.message(data_json['data']['id'])
                return 'Signature verified',200
        else:
            return 'Bad signature',400
       

@app.route('/attachment', methods=['POST'])
def handle_attachment():
    '''
    STUB
    '''
    if request.method == 'POST':
        data_raw = request.data
        signature_from_webex=request.headers.get('X-Spark-Signature')
        hashed_by_module = hmac.new(secret_key.encode(), data_raw, hashlib.sha1).hexdigest()
                
        if signature_from_webex==hashed_by_module:
            return 'Signature verified',200
        else:
            return 'Bad signature',400

@app.route('/memberships', methods=['POST'])
def handle_event():
    '''
    STUB
    '''
    if request.method == 'POST':
        data_raw = request.data
        signature_from_webex=request.headers.get('X-Spark-Signature')
        hashed_by_module = hmac.new(secret_key.encode(), data_raw, hashlib.sha1).hexdigest()
                
        if signature_from_webex==hashed_by_module:
            return 'Signature verified',200
        else:
            return 'Bad signature',400

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
