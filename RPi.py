import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(40, GPIO.OUT)

"""
for i in range(5):
    GPIO.output(40, GPIO.HIGH)
    print("on")
    time.sleep(1)
    GPIO.output(40, GPIO.LOW)
    print("off")
    time.sleep(1)
    """

GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)

"""
# This will turn the LED light on while you press down the button
while True:
    input_state = GPIO.input(38)
    if input_state == False:
        print("Button Pressed")
        GPIO.output(40, GPIO.HIGH)
    else:
        GPIO.output(40, GPIO.LOW)
"""

# This will turn the LED light on while you toggle back and off
lightStatus = False
GPIO.output(40, GPIO.LOW)

while True:
    input_state = GPIO.input(38)
    if input_state == False:
        print("button has been pressed")
        time.sleep(.3)
        if lightStatus == False:
            GPIO.output(40, GPIO.HIGH)
            lightStatus = True
        else:
            GPIO.output(40, GPIO.LOW)
            lightStatus = False
