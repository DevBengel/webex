'''
This is the main server module. Within this module we check incoming post Messages
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
import init_lab
import atexit

#Preparing the environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), 'config/.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
secret_key=str(os.getenv('HOOKSECRET'))

# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def exit_handler():
    print("Exiting module. Clean-up code executed.")
    init_lab.de_init() 

# Register the exit_handler function to be called when the module exits
atexit.register(exit_handler)

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
                controller.message(data_json['data']['id'],data_json['data']['roomId'])
                return 'Signature verified',200
            else:
                print ("Found a message from myself...")
                return 'Understood but ignored- because its the bot speaking to himself',200
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
    init_lab.init()
    app.run(debug=True,use_reloader=False)
