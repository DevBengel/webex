import requests
import json

def chuckjoke():

    url = "https://api.chucknorris.io/jokes/random"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = json.loads(response.text)

    return(response_json['value'])

if __name__=='__main__':
    print(chuckjoke())
