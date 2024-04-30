from dotenv import load_dotenv
import requests
import json
import os
import logging
import time
from datetime import datetime

dotenv_path = os.path.join(os.path.dirname(__file__), '../config/.env')
load_dotenv(dotenv_path)

year=2024
month=4
day=30
hour=8
minute=0
second=0
microsecond=0


def get_time():
    dt = datetime(year, month, day, hour, minute, second, microsecond)
    iso_date = dt.isoformat()
    return (iso_date)

start = get_time()
hour=hour+1
end = get_time()

print (start)
print (end)


