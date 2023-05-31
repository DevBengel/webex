import os
import logging
from dotenv import load_dotenv
from webex import webhooks

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

# Configure the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


print(webhooks.create_webhook('DelMe',os.getenv('NGROKURL')+'/messages','messages','created',os.getenv('HOOKSECRET')))
