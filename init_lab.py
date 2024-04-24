'''
This is the lab init module. It is used to register all needed webhooks.
We call it from the main module 
'''
import os
import json
from pathlib import Path
from dotenv import load_dotenv, set_key
from webex import webhooks, people
from ngrok_setup import ngrok_start




def load_environment():
    '''
    It just loads the environment variables
    '''
    dotenv_path = os.path.join(os.path.dirname(__file__), 'config/.env')
    load_dotenv(dotenv_path)
    return Path(dotenv_path)

def delete_old_hooks():
    '''
    For housekeeping i delete all old webhooks, everytime we start or stop the main module
    '''
    webhooks_json = json.loads(webhooks.list_webhooks())
    for webhook in webhooks_json['items']:
        if 'delme' in webhook['name'].lower():
            print(f"Deleting webhook: {webhook['name']}")
            webhooks.delete_webhook(webhook['id'])

def generate_fresh_hooks(tunnel_url):
    '''
    Generating new webhooks, everytime we initialize the bot
    '''
    hook_secret = os.getenv('HOOKSECRET')
    if tunnel_url and hook_secret:
        #create a new webhook for messages
        print(webhooks.create_webhook('DelMe', f'{tunnel_url}/messages', 'messages', 'created', hook_secret))
        #create a new webhook for attachments - this is needed for adaptive cards
        print(webhooks.create_webhook('DelMe', f'{tunnel_url}/attachment','attachmentActions','created',hook_secret))
    else:
        print("NGROKURL or HOOKSECRET environment variable not found. Unable to generate new hooks.")



def set_bot_mail_variable():
    '''
    The bot receives messages with its own Nickname in front of the text if in a group chat.
    Therefore i search for the Nickname in other modules.
    Quick and dirty, this function copys relevant infos to the .env file
    '''
    env_file_path = load_environment()
    person_email = people.myemail()
    person_nickname = people.my_Nick_Name()
    if person_email:
        print(f"Setting filter Email to {person_email}")
        set_key(dotenv_path=env_file_path, key_to_set="BOTMAIL", value_to_set=person_email)
    else:
        print("Unable to retrieve bot email. Check your Webex API configuration.")
    if person_nickname:
        print(f"Setting filter Nickname to {person_nickname}")
        set_key(dotenv_path=env_file_path, key_to_set="NICKNAME", value_to_set=person_nickname)
    else:
        print("Unable to retrieve bot email. Check your Webex API configuration.")

def init():
    '''
    Initializing the demo
    '''
    delete_old_hooks()
    tunnel_url=ngrok_start.main()
    generate_fresh_hooks(tunnel_url)
    set_bot_mail_variable()

def de_init():
    '''
    cleaning everything up, after the demo.
    '''
    delete_old_hooks()
    print("Deleting old ngrok tunnels")
    ngrok_start.disconnect()


if __name__ == "__main__":
    #just for manual testing
    init()
    de_init()
