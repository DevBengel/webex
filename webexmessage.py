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

def get_Message(messageID):
    #print ('Ich suche die Nachricht mit der ID : '+messageID)
    apiUrl = "https://webexapis.com/v1/messages/"+messageID
    access_token = str(os.getenv("ACCESSTOKEN"))
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body = {}
    response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
    data=json.loads(response.text)
    #print (data['personEmail'] + ' schrieb: ' + data['text'])
    
    return(data['text'])

if __name__=='__main__':
    print(send_message(os.getenv('TARGETEMAIL'),'test'))

