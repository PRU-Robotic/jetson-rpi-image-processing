from time import sleep
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

# Initialise servo
pigpio_factory = PiGPIOFactory()

#servo = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)
servo1 = AngularServo(18, pin_factory=pigpio_factory)
servo1_now = 0
servo1.angle = servo1_now

if (servo1_now>90 or servo1_now<-90):
    servo1_now = 0        
    servo1.angle = servo1_now
    sleep(0.00001)

servo1.angle = 90

sleep(2)

servo1.angle = 0

sleep(2)

servo1.angle = -90

"""
Araç düz sırada ilerlerken, nesne tespit gerçekleştiğinde;
    - bitkiye döner,
    - ortaya döner,
    - sonra diğer sıradaki bitkiye döner
    
    (for döngüsünde bu sürdürebilirlik sağlanmalı)
"""