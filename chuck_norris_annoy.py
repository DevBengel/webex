import chuck_norris.chuck_norris_jokes as chuck_norris_jokes
import webex.webexmessage as webexmessage
import os

for i in range (10):
    joke=chuck_norris_jokes.chuckjoke(name='John Doe',category='dev')
    print(webexmessage.send_message(os.getenv('TARGETEMAIL'),joke))