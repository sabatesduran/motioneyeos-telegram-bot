import os
from dotenv import load_dotenv

load_dotenv()

SERVO_ANGLE_MIN = os.getenv('SERVO_ANGLE_MIN')
SERVO_ANGLE_MAX = os.getenv('SERVO_ANGLE_MAX')
SERVOS_CONFIG_FILE = os.getenv('SERVOS_CONFIG_FILE')
VERTICAL_SERVO_PIN = os.getenv('VERTICAL_SERVO_PIN')
HORITZONTAL_SERVO_PIN = os.getenv('HORITZONTAL_SERVO_PIN')
DEFAULT_SERVO_MOVEMENT = os.getenv('DEFAULT_SERVO_MOVEMENT')