from dotenv import load_dotenv,set_key
import requests
import json
import os
import logging

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

reqUrl = "https://webexapis.com/v1/devices"


def renew_access_token():


    reqUrl = "https://webexapis.com/v1/access_token"

    headersList = {
    "Content-Type": "application/x-www-form-urlencoded" 
    }
    payload = f"grant_type=refresh_token&client_id={os.getenv('CLIENT_ID')}&client_secret={os.getenv('CLIENT_SECRET')}&refresh_token={os.getenv('REFRESH_TOKEN')}"

    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
    response_json=json.loads(response.text)

    print('Access Token renewed')
    set_key(dotenv_path=dotenv_path, key_to_set="ACCESS_TOKEN", value_to_set=response_json['access_token'])
    set_key(dotenv_path=dotenv_path, key_to_set="REFRESH_TOKEN", value_to_set=response_json['refresh_token'])
    
    return response.text


def get_devices():
    ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
    headersList = {
    "Authorization": "Bearer "+ACCESS_TOKEN
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

    return(response.text)


if __name__=="__main__":
    print(renew_access_token())
