'''
This module is meant for bringing the samples to life. The module takes care of a maybe present Nickname first.
'''
from webex import webexmessage
from chuck_norris import chuck_norris_jokes
import os
from dotenv import load_dotenv


load_dotenv()



buzzword_list=['joke','ping','card']

def message(message_ID,roomId):
    '''
    First a way to deal with messages right now- it just prints it out
    Eventually, there is a nickname before the string. the function check_for_nickname
    will delete it if present.
    '''
    message=check_for_nickname(webexmessage.get_Message(message_ID))
    
    if message in buzzword_list:
        print(f"Buzzword detected! {message}")
        if message == 'joke':
            handle_joke(roomId)
        elif message == 'ping':
            handle_ping()
        elif message == 'card':
            handle_card()

    else:
        print (f"Normal Message {message}")

def check_for_nickname(message):
    nickname=os.environ.get('NICKNAME')
    original_string = message
    substring_to_remove = f"{nickname} "  # Note the space after "Nickname"

    # Check if the substring is in the original string
    if substring_to_remove in original_string:
        # Remove the substring
        result_string = original_string.replace(substring_to_remove, "")
    else:
        result_string = original_string

    return (result_string)


def handle_ping():
    print ("PONG")
    return None

def handle_joke(roomId):
    webexmessage.send_message_to_roomid(roomId,chuck_norris_jokes.chuckjoke())
    return None

def handle_card():
    print ("Adaptive")
    return None
