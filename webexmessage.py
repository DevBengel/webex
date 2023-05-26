import requests
import json
import os

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

if __name__=='__main__':
    print(send_message(os.getenv('TARGETEMAIL'),'test'))

