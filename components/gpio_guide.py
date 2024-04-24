import RPI.GPIO as GPIO
from time import sleep

# disable warning messages in terminal
GPIO.setwarnings(False)

# set pin numbering mode to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# configure a specific pin as output pin
pin_number = 11  #replace with the actual pin number you want to control
GPIO.setup(pin_number, GPIO.OUT, initial=GPIO.LOW) #initial parameter is optional


while True:
    #set the pin to HIGH (3.3V) state
    GPIO.output(pin_number, GPIO.HIGH)
    
    # pause for 1 second
    sleep(1)

    # set the pin to LOW (0V) state
    GPIO.output(pin_number, GPIO.LOW)

    # pause for another 1 second
    sleep(1)