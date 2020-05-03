import sys
from gpiozero import AngularServo
from time import sleep

SERVO = sys.argv[1]
TO_POSITION = sys.argv[2]

V_SERVO_PIN = 12
H_SERVO_PIN = 13


def move(with_servo, to_position):
    if to_position == 'mid':
        with_servo.mid()
    elif to_position == 'max':
        with_servo.max()
    elif to_position == 'min':
        with_servo.min()

    sleep(0.5)


if SERVO == 'v':
    pin = V_SERVO_PIN
else:
    pin = H_SERVO_PIN

move(AngularServo(pin), TO_POSITION)
