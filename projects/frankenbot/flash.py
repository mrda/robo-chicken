#
# Test circuit flashing a LED on a
# https://www.adafruit.com/products/2928
#
# See https://github.com/adafruit/micropython-adafruit-pca9685 for inspiration
#
import machine
import pca9685

CHANNEL = 0

i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
pca = pca9685.PCA9685(i2c)


def flash(p, state):
    # Note(mrda): Frequency is not per channel
    if state:
        p.freq(12)
    else:
        p.freq(60)


def brightness_walk(channel, p):
    for d in range(0, 4095):  # 12 bits here, 0-4095
        p.duty(channel, d)


while True:
    flash(pca, True)
    brightness_walk(CHANNEL, pca)
    flash(pca, False)
    brightness_walk(CHANNEL, pca)
