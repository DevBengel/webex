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

baseurl = "https://webexapis.com/v1/attachment/actions/"

def get_attachment(attachment_id):
    url=baseurl+attachment_id
    access_token = str(os.getenv("ACCESSTOKEN"))
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body = {}
    response = requests.get(url=url, json=body, headers=httpHeaders)
    data=json.loads(response.text)

    return data

if __name__=="__main__":
    print(get_attachment('Y2lzY29zcGFyazovL3VzL0FUVEFDSE1FTlRfQUNUSU9OLzQ0ZDI5ODUwLTAxNmQtMTFlZi05Njk2LTk1OTQ3NTA1NmUxNA'))


