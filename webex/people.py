'''
In this module i provide some functions for the "people" endpoint.
I need it to initialize the lab correctly
'''

from dotenv import load_dotenv
import requests
import os
import json

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

def myemail():

    url = "https://webexapis.com/v1/people/me"

    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    email=response_json['emails'][0]

    return(email)

def my_Nick_Name():

    url = "https://webexapis.com/v1/people/me"

    payload = {}
    headers = {
    'Authorization': 'Bearer ' + str(os.getenv('ACCESSTOKEN')),
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    nickName=response_json['nickName']

    return(nickName)


if __name__=="__main__":
    print(myemail())
