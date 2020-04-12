import os
import json
from dotenv import load_dotenv

load_dotenv()

LIST_OF_ADMINS = json.loads(os.getenv('LIST_OF_ADMINS'))
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
MOTIONEYEOS_URL = os.getenv('MOTIONEYEOS_URL')
MOTIONEYEOS_USER =  os.getenv('MOTIONEYEOS_USER')
MOTIONEYEOS_API_KEY =  os.getenv('MOTIONEYEOS_API_KEY')

def get_list_of_admins():
  return [int(admin) for admin in LIST_OF_ADMINS]