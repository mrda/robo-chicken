from machine import I2C, Pin
import time


class SimpleMatrix8x8:
    """
    Driver for AdaFruit 8x8 LED Matrix display with HT16K33 backpack.

    Based on https://github.com/r1chardj0n3s/micropython-matrix8x8/
    """

    GREEN = 0
    RED = 1
    ORANGE = 2

    GREEN_ROW_ADDR = (0x00, 0x02, 0x04, 0x06, 0x08, 0x0A, 0x0C, 0x0E)
    RED_ROW_ADDR = (0x01, 0x03, 0x05, 0x07, 0x09, 0x0B, 0x0D, 0x0F)

    def __init__(self, i2c_bus=1, addr=0x70, brightness=15, i2c=None):
        """
        Params:
        * i2c_bus = I2C bus ID (1 or 2) or None (if param 'i2c' is provided)
        * addr = I2C address of connected display
        * brightness = display brightness (0 - 15)
        * i2c = initialised instance of pyb.I2C object
        """
        self._blinking = 0
        self.addr = addr
        self.green_buf = bytearray(8)
        self.red_buf = bytearray(8)
        self.is_on = False

        # I2C init
        if i2c:
            self.i2c = i2c
        else:
            self.i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
            self.i2c.start()

        # set HT16K33 oscillator on
        self._send(b'\x21')

        self.set_brightness(brightness)
        self.clear()
        self.on()

    def _send(self, data):
        """
        Send data over I2C.
        """
        self.i2c.writeto(self.addr, data)

    def _send_row(self, row):
        """
        Send single row over I2C.
        """
        green_data = bytes((self.GREEN_ROW_ADDR[row], self.green_buf[row]))
        red_data = bytes((self.RED_ROW_ADDR[row], self.red_buf[row]))
        self._send(green_data)
        self._send(red_data)

    def _send_buf(self):
        """
        Send buffer over I2C.
        """
        #TODO(mrda): Build the buffer up here and do one write
        #self._send(self.green_buf)
        #self._send(self.red_buf)
        for row in range(8):
            self._send_row(row)

    def on(self):
        """
        Turn on display.
        """
        self.is_on = True
        self._send(bytes([0x81 | self._blinking << 1]))

    def off(self):
        """
        Turn off display. You can controll display when it's off (change image,
        brightness, blinking, ...).
        """
        self.is_on = False
        self._send(b'\x80')

    def set_brightness(self, value):
        """
        Set display brightness. Value from 0 (min) to 15 (max).
        """
        self._send(bytes([0xE0 | value]))

    def clear(self):
        """
        Clear display.
        """

        for i in range(8):
            self.green_buf[i] = 0
            self.red_buf[i] = 0
        self._send_buf()
