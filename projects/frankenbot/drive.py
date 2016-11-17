#
# Test circuit to drive Frakenbot in a pseudo-racetrack
# Making use of a ESP8266 Huzzah running micropython and using
# https://www.adafruit.com/products/2928
#
# See https://github.com/adafruit/micropython-adafruit-pca9685 and
# https://learn.adafruit.com/adafruit-arduino-lesson-13-dc-motors/...
# .../breadboard-layout for inspiration
#
import machine
import pca9685
import time


# Channel defs
LEFT = 3
RIGHT = 0

# Speed defs
SPEED_OFF = 0
SPEED_SLOW = 1024
SPEED_RUN = 2048
SPEED_FAST = 4095  # Maximum

TURN_TIME = 1


class RoboDrive:

    def __init__(self, i2c=None, address=0x40, freq=40):
        if i2c is not None:
            self.i2c = i2c
        else:
            self.i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
        self.pca = pca9685.PCA9685(self.i2c, address)
        self.pca.freq(freq)

    def step(self, secs=None, speed=None):
        if speed is None:
            speed = SPEED_FAST
        if secs is None:
            secs = 2
        self.pca.duty(LEFT, speed)
        self.pca.duty(RIGHT, speed)
        time.sleep(secs)
        self.pca.duty(LEFT, SPEED_OFF)
        self.pca.duty(RIGHT, SPEED_OFF)

    def turn_left(self):
        # TODO(mrda): Use the optical encoders, rather than guessing
        self.pca.duty(RIGHT, SPEED_OFF)
        self.pca.duty(LEFT, SPEED_FAST)
        time.sleep(TURN_TIME)
        self.pca.duty(LEFT, SPEED_OFF)
        self.pca.duty(RIGHT, SPEED_OFF)

    def turn_right(self):
        # TODO(mrda): Use the optical encoders, rather than guessing
        self.pca.duty(LEFT, SPEED_OFF)
        self.pca.duty(RIGHT, SPEED_FAST)
        time.sleep(TURN_TIME)
        self.pca.duty(LEFT, SPEED_OFF)
        self.pca.duty(RIGHT, SPEED_OFF)
