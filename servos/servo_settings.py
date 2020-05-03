import os
from dotenv import load_dotenv

load_dotenv()

SERVO_ANGLE_MIN = float(os.getenv('SERVO_ANGLE_MIN'))
SERVO_ANGLE_MAX = float(os.getenv('SERVO_ANGLE_MAX'))
VERTICAL_SERVO_PIN = int(os.getenv('VERTICAL_SERVO_PIN'))
HORITZONTAL_SERVO_PIN = int(os.getenv('HORITZONTAL_SERVO_PIN'))
SERVOS_CONFIG_FILE = os.getenv('SERVOS_CONFIG_FILE')
DEFAULT_SERVO_MOVEMENT = os.getenv('DEFAULT_SERVO_MOVEMENT')