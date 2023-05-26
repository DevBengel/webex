import chuck
import webexmessage
import os

for i in range (10):
    joke=chuck.chuckjoke()
    print(webexmessage.send_message(os.getenv('TARGETEMAIL'),joke))