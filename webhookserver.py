# Dieses File dient nur zur Demonstration von Webhooks. Ein eingerichteter Webhook feuert auf
# den hier implementierten Server. Nach Eingang des Webhooks, holt sich das System den
# eingegebenen Text und wirft diesen auf der Konsole aus.

from flask import Flask, request
import json
import webexmessage

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='GET':
        return ('Webserver für simple Webhooks', 200, None)
    
    if request.method=='POST':
          
        data=json.loads(request.data)
        print('Webhookdaten : '+ str(data))
        print (data['data']['id'])
        messageID=data['data']['id']
        webexmessage.getMessage(messageID)
        return '{"success":"true"}'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
