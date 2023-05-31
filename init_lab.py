from webex import webhooks
import json
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

def delete_old_hooks():
    webhooks_json=json.loads(webhooks.list_webhooks())

    for counter, webhook in enumerate(webhooks_json['items']):
        if 'delme' in webhook['name'] or 'DelMe' in webhook['name']:
            print(webhooks.delete_webhook(webhook['id']))
    
def generate_fresh_hooks():
    print(webhooks.create_webhook('DelMe',os.getenv('NGROKURL')+'/messages','messages','created',os.getenv('HOOKSECRET')))


delete_old_hooks()
generate_fresh_hooks()
