from webex import webhooks
import json

webhooks_json=json.loads(webhooks.list_webhooks())

for counter, webhook in enumerate(webhooks_json['items']):
    if 'del' in webhook['name'] or 'Del' in webhook['name']:
        print(webhooks.delete_webhook(webhook['id']))
    

