import time
import Adafruit_ADS1x15
import board, busio
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX

# Create ADC instances
adc_a = Adafruit_ADS1x15.ADS1015(address=0x48)
adc_b = Adafruit_ADS1x15.ADS1015(address=0x49)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = LSM6DSOX(i2c)

# Constants
GAIN = 1

while True:
	print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (sensor.acceleration))
	print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
	#print("")
	#print("ADC A, Analog 0 ", adc_a.read_adc(0, gain=GAIN))
	#print("ADC B, Analog 0 ", adc_b.read_adc(0, gain=GAIN))
	#time.sleep(.25)
