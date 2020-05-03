import os.path
import sys
import json

from gpiozero import AngularServo
from time import sleep
from servo_settings import *

DIRECTION = sys.argv[1]

def get_config():
    if os.path.isfile(SERVOS_CONFIG_FILE):
        with open(SERVOS_CONFIG_FILE) as f:
            config = json.load(f)
    else:
        with open(SERVOS_CONFIG_FILE, 'w') as f:
            config = {
                'VERTICAL_POSITION': 0,
                'HORITZONTAL_POSITION': 0
            }
            json.dump(config, f)
        
    return config

def write_current_servo_angle_to_file(servo, angle):
    config = get_config()
    config[servo] = angle
    with open(SERVOS_CONFIG_FILE, 'w') as f:
        json.dump(config, f)


def get_current_angle_from_servo():        
    servo = get_servo_pin_from_direction()
    
    config = get_config()

    return float(config[servo['key']])


def get_servo_pin_from_direction():
    if DIRECTION in ['up', 'down']:
        return {
            'key': 'VERTICAL_POSITION',
            'pin': VERTICAL_SERVO_PIN
        }
    elif DIRECTION in ['right', 'left']:
         return {
            'key': 'HORITZONTAL_POSITION',
            'pin': HORITZONTAL_SERVO_PIN
        }
    
    return None

def get_new_angle(min_or_max, current_angle, angle):
    if min_or_max == 'min':
        new_angle = current_angle - angle
        return SERVO_ANGLE_MIN if new_angle <= SERVO_ANGLE_MIN else new_angle
    elif min_or_max == 'max':
        new_angle = current_angle + angle
        return SERVO_ANGLE_MAX if new_angle >= SERVO_ANGLE_MAX else new_angle

def move(with_servo, angle):
    servo = get_servo_pin_from_direction()
    current_angle = get_current_angle_from_servo()

    if DIRECTION in ['up', 'right']:
        with_servo.angle = get_new_angle('min', current_angle, angle)
    elif DIRECTION in ['down', 'left']:
        with_servo.angle = get_new_angle('max', current_angle, angle)
    elif DIRECTION == 'home':
        with_servo.mid()

    sleep(1)

    write_current_servo_angle_to_file(servo['key'], with_servo.angle)


def main():
    try:
        angle = float(sys.argv[2])
    except Exception:
        print(f"Angle movement set to default ({DEFAULT_SERVO_MOVEMENT})")
        angle = float(DEFAULT_SERVO_MOVEMENT)

    servo_info = get_servo_pin_from_direction()
    if servo_info is not None:
        servo = AngularServo(
            servo_info['pin'],
            min_angle=SERVO_ANGLE_MIN,
            max_angle=SERVO_ANGLE_MAX,
            min_pulse_width=0.0006,
            max_pulse_width=0.0024
        )
        print(servo.angle)
        move(servo, angle)
    else:
        print("The available directions are: up, down, right and left.")
    
    print(servo.angle)


# Execute script
main()