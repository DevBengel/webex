from dotenv import load_dotenv
import requests
import os
import json

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

def list_webhooks():

    url = "https://webexapis.com/v1/webhooks"

    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)


def delete_webhook(webhook_id):

    url = f"https://webexapis.com/v1/webhooks/{webhook_id}"

    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    return(response.status_code)


def create_webhook(name,targeturl,resource,event,secret):
    
    url = f"https://webexapis.com/v1/webhooks"

    payload = json.dumps({
    "name": name,
    "targetUrl": targeturl,
    "resource": resource,
    "event":event,
    "secret":secret
    })

    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response.text)
    


if __name__=="__main__":
    print(list_webhooks())
