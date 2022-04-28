import time
import Adafruit_ADS1x15
import board, busio
import RPi.GPIO as GPIO
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

from Wearable import *

# Create ADC instances
#adc_a = Adafruit_ADS1x15.ADS1015(address=0x48)
adc_b = Adafruit_ADS1x15.ADS1015(address=0x49)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = LSM6DSOX(i2c)

# Constants
GAIN = 1
BTN_1 = 17
BTN_2 = 27
LED = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BTN_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BTN_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


glove = Wearable()

glove.add_input(Input("Thumb", "analog"))
glove.add_input(Input("Index", "analog"))

thumb = lambda: adc_b.read_adc(0, gain=GAIN)
index = lambda: adc_b.read_adc(1, gain=GAIN)
print(glove.inputs[0].set_source(thumb))
print(glove.inputs[1].set_source(index))

led = False

while True:
    if (GPIO.input(BTN_1) == GPIO.HIGH):
        print("Button 1 pressed")
        if (not led):
            GPIO.output(LED, GPIO.HIGH)
            led = True
        else:
            led = False
    if (GPIO.input(BTN_2) == GPIO.HIGH):
        print("Button 2 pressed")
        if (not led):
            GPIO.output(LED, GPIO.HIGH)
            led = True
        else:
            led = False
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
    print(" ")
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
    print(" ")
    print("ADC B, Analog 0", glove.inputs[0].read())
    print("ADC B, Analog 1", glove.inputs[1].read())
    GPIO.output(LED, GPIO.LOW)
    time.sleep(.5)
