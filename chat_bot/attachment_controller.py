import json
from webex import webex_attachments

def handle_attachment(action_item_id):
    attachment = webex_attachments.get_attachment(action_item_id)

    print('These are the inputs given in the card: ')    
    # Print the values of the items in attachment_data['inputs']
    for key, value in attachment['inputs'].items():
        print(f'{key} : {value}')

    return None