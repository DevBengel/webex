'''
This module is meant for bringing the samples to life. 
'''
from webex import webexmessage

def message(message_ID):
    '''
    First a way to deal with messages right now- it just prints it out
    '''
    message=webexmessage.get_Message(message_ID)
    print (message)

