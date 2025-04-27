import os
import requests
from dotenv import load_dotenv
from utils.logger import log_and_print

load_dotenv()

PUSHOVER_APP_TOKEN = os.getenv('PUSHOVER_APP_TOKEN')
PUSHOVER_USER_KEY = os.getenv('PUSHOVER_USER_KEY')

def send_notification(title, message):
    if not PUSHOVER_APP_TOKEN or not PUSHOVER_USER_KEY:
        print("Missing Pushover credentials! Notification not sent.")
        return
    
    data = {
        "token": PUSHOVER_APP_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "title": title,
        "message": message
    }

    response = requests.post("https://api.pushover.net/1/messages.json", data=data)

    if response.status_code != 200:
        log_and_print(f"Failed to send notification: {response.text}", "error")