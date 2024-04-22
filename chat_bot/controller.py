'''
This module is meant for bringing the samples to life. The module takes care of a maybe present Nickname first.
'''
from webex import webexmessage
import os
from dotenv import load_dotenv

buzzword_list=['joke','ping']

def message(message_ID):
    '''
    First a way to deal with messages right now- it just prints it out
    Eventually, there is a nickname before the string. the function check_for_nickname
    will delete it if present.
    '''
    message=check_for_nickname(webexmessage.get_Message(message_ID))
    
    if message in buzzword_list:
        print(f"Buzzword detected! {message}")
        if message == 'joke':
            handle_joke()
        elif message == 'ping':
            handle_ping()

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

def handle_joke():
    print ("Haha")
