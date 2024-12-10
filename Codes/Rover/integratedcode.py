import RPi.GPIO as GPIO
import serial
import time
from time import sleep

in1_motor1 = 24
in2_motor1 = 23
en_motor1 = 25

in1_motor2 = 17
in2_motor2 = 27
en_motor2 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1_motor1, GPIO.OUT)
GPIO.setup(in2_motor1, GPIO.OUT)
GPIO.setup(en_motor1, GPIO.OUT)
GPIO.output(in1_motor1, GPIO.LOW)
GPIO.output(in2_motor1, GPIO.LOW)
p_motor1 = GPIO.PWM(en_motor1, 1000)

GPIO.setup(in1_motor2, GPIO.OUT)
GPIO.setup(in2_motor2, GPIO.OUT)
GPIO.setup(en_motor2, GPIO.OUT)
GPIO.output(in1_motor2, GPIO.LOW)
GPIO.output(in2_motor2, GPIO.LOW)
p_motor2 = GPIO.PWM(en_motor2, 1000)

p_motor1.start(25)
p_motor2.start(25)

bluetooth_port = '/dev/ttyAMA0'
baud_rate = 9600

bluetooth = serial.Serial(bluetooth_port, baud_rate)
time.sleep(2)

print("R-right L-left S-stop F-forward B-backward W-low U-medium V-high e-exit\n")

while True:
    x = bluetooth.read().decode('latin-1')

    if x == 'F':
        print("forward")
        GPIO.output(in1_motor1, GPIO.LOW)
        GPIO.output(in2_motor1, GPIO.HIGH)
        GPIO.output(in1_motor2, GPIO.LOW)
        GPIO.output(in2_motor2, GPIO.HIGH)
        x = 'z'

    elif x == 'B':
        print("backward")
        GPIO.output(in1_motor1, GPIO.HIGH)
        GPIO.output(in2_motor1, GPIO.LOW)
        GPIO.output(in1_motor2, GPIO.HIGH)
        GPIO.output(in2_motor2, GPIO.LOW)
        x = 'z'

    elif x == 'R':
        print("right")
        GPIO.output(in1_motor1, GPIO.LOW)
        GPIO.output(in2_motor1, GPIO.HIGH)
        GPIO.output(in1_motor2, GPIO.HIGH)
        GPIO.output(in2_motor2, GPIO.LOW)
        x = 'z'

    elif x == 'L':
        print("left")
        GPIO.output(in1_motor1, GPIO.HIGH)
        GPIO.output(in2_motor1, GPIO.LOW)
        GPIO.output(in1_motor2, GPIO.LOW)
        GPIO.output(in2_motor2, GPIO.HIGH)
        x = 'z'

    elif x == 'S':
        print("stop")
        GPIO.output(in1_motor1, GPIO.LOW)
        GPIO.output(in2_motor1, GPIO.LOW)
        GPIO.output(in1_motor2, GPIO.LOW)
        GPIO.output(in2_motor2, GPIO.LOW)
        x = 'z'

    elif x == 'W':
        print("low")
        p_motor1.ChangeDutyCycle(25)
        p_motor2.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'U':
        print("medium")
        p_motor1.ChangeDutyCycle(50)
        p_motor2.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'V':
        print("high")
        p_motor1.ChangeDutyCycle(75)
        p_motor2.ChangeDutyCycle(75)
        x = 'z'

    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
