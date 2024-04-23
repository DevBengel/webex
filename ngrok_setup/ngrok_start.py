# import ngrok python sdk
import ngrok
import os
from dotenv import load_dotenv
import time

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

def create_tunnel():
    # Establish connectivity
    listener = ngrok.forward(5000, authtoken=os.getenv('NGROK_AUTHTOKEN'))

    # Output ngrok url to console
    print(f"Ingress established at {listener.url()}")
    return listener.url()

def disconnect():
    ngrok.disconnect()

def main():
    disconnect()
    time.sleep(3)
    tunnel_url = create_tunnel()
    print(tunnel_url)
    return tunnel_url

if __name__=="__main__":
    main()