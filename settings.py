import os
import json
from dotenv import load_dotenv

load_dotenv()

# BOT
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
MOTIONEYEOS_URL = os.getenv('MOTIONEYEOS_URL')
MOTIONEYEOS_USER =  os.getenv('MOTIONEYEOS_USER')
MOTIONEYEOS_API_KEY =  os.getenv('MOTIONEYEOS_API_KEY')

def get_list_of_admins():
  admins = json.loads(os.getenv('LIST_OF_ADMINS'))
  return [int(admin) for admin in admins]

# SERVOS
SERVO_ANGLE_MIN = os.getenv('SERVO_ANGLE_MIN')
SERVO_ANGLE_MAX = os.getenv('SERVO_ANGLE_MAX')
SERVOS_CONFIG_FILE = os.getenv('SERVOS_CONFIG_FILE')
VERTICAL_SERVO_PIN = os.getenv('VERTICAL_SERVO_PIN')
HORITZONTAL_SERVO_PIN = os.getenv('HORITZONTAL_SERVO_PIN')
DEFAULT_SERVO_MOVEMENT = os.getenv('DEFAULT_SERVO_MOVEMENT')