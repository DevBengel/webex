from dotenv import load_dotenv
import requests
import json
import os
import logging

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_message(email,text):

    url = "https://webexapis.com/v1/messages"

    payload = json.dumps({
    "toPersonEmail": email,
    "text": text
    })
    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response.text)


def send_message_to_roomid(roomid,text):

    url = "https://webexapis.com/v1/messages"

    payload = json.dumps({
    "roomId": roomid,
    "text": text
    })
    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response.text)

def send_message_to_roomid_md(roomid,md):

    url = "https://webexapis.com/v1/messages"

    payload = json.dumps({
    "roomId": roomid,
    "markdown": md
    })
    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response.text)


def get_Message(messageID):
    print ('Searching for Message with ID: '+messageID)
    apiUrl = "https://webexapis.com/v1/messages/"+messageID
    access_token = str(os.getenv("ACCESSTOKEN"))
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body = {}
    response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
    data=json.loads(response.text)
        
    return(data['text'])



if __name__=='__main__':
    logger.info(send_message(os.getenv('TARGETEMAIL'),'test'))

