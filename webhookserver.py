# Dieses File dient nur zur Demonstration von Webhooks. Ein eingerichteter Webhook feuert auf
# den hier implementierten Server. Nach Eingang des Webhooks, holt sich das System den
# eingegebenen Text und wirft diesen auf der Konsole aus.

from flask import Flask, request
import json
import os
import requests

app = Flask(__name__)

def getMessage(messageID):
    print ('Ich suche die Nachricht mit der ID : '+messageID)
    apiUrl = "https://webexapis.com/v1/messages/"+messageID
    access_token = os.getenv("ACCESSTOKEN")
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body = {}
    response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
    data=json.loads(response.text)
    print (data['personEmail'] + ' schrieb: ' + data['text'])
    #print (data)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='GET':
        return ('Webserver für simple Webhooks', 200, None)
    
    if request.method=='POST':
          
        data=json.loads(request.data)
        print('Webhookdaten : '+ str(data))
        print (data['data']['id'])
        messageID=data['data']['id']
        getMessage(messageID)
        return '{"success":"true"}'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
