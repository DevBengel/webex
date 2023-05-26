import chuck
import webexmessage

for i in range (10):
    joke=chuck.chuckjoke()
    print(webexmessage.send_message("targetemail@targetdomain",joke))