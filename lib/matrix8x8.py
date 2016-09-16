from machine import I2C, Pin
import time


class Matrix8x8:
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

    def _clear_column(self, column):
        """
        Clear column in buffer (set it to 0).
        """
        mask = 0x80 >> column
        for row in range(8):
            if self.green_buf[row] & mask:
                self.green_buf[row] ^= mask
            if self.red_buf[row] & mask:
                self.red_buf[row] ^= mask

    def _set_column(self, column, green_byte, red_byte):
        """
        Set column in buffer by byte.
        """
        self._clear_column(column)
        if green_byte == 0 and red_byte == 0:
            return
        mask = 0x80
        for row in range(8):
            shift = column - row
            if shift >= 0:
                self.green_buf[row] |= (green_byte & mask) >> shift
                self.red_buf[row] |= (red_byte & mask) >> shift
            else:
                self.green_buf[row] |= (green_byte & mask) << abs(shift)
                self.red_buf[row] |= (red_byte & mask) << abs(shift)
            mask >>= 1

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

    def set_blinking(self, mode):
        """
        Set blinking. Modes:
            0 - blinking off
            1 - blinking at 2Hz
            2 - blinking at 1Hz
            3 - blinking at 0.5Hz
        """
        self._blinking = mode
        if self.is_on:
            self.on()

    def set(self, green_bitmap, red_bitmap):
        """
        Show bitmap on display. Bitmap should be 16 bytes/bytearray object or any
        iterable object containing 2x 8 bytes (one byte per row per color).
        """
        self.green_buf = bytearray(green_bitmap)
        self.red_buf = bytearray(red_bitmap)
        self._send_buf()

    def clear(self):
        """
        Clear display.
        """
        # Stop blinking
        self.set_blinking(0)

        for i in range(8):
            self.green_buf[i] = 0
            self.red_buf[i] = 0
        self._send_buf()

    def set_row_by_byte(self, row, green_byte, red_byte):
        """
        Set row by byte.
        """
        self.green_buf[row] = green_byte
        self.red_buf[row] = red_byte
        self._send_row(row)

    def set_row_by_color(self, row, byte, color):
        """
        Set row by byte.
        """
        if color == self.GREEN:
            self.green_buf[row] = byte
            self.red_buf[row] = 0x00
        elif color == self.RED:
            self.green_buf[row] = 0x00
            self.red_buf[row] = byte
        else:
            self.green_buf[row] = byte
            self.red_buf[row] = byte
        self._send_row(row)

    def clear_row(self, row):
        """
        Clear row.
        """
        self.set_row_by_color(row, 0x00, 0x00)

    def set_column_by_byte(self, column, green_byte, red_byte):
        """
        Set column by byte.
        """
        self._set_column(column, green_byte, red_byte)
        self._send_buf()

    def clear_column(self, column):
        """
        Clear column.
        """
        self._clear_column(column)
        self._send_buf()

    def set_pixel(self, row, column, color):
        """
        Set (turn on) pixel.
        """
        if color == self.GREEN:
            self.green_buf[row] |= (0x80 >> column)
            self.red_buf[row] &= ~(0x80 >> column)
        elif color == self.RED:
            self.red_buf[row] |= (0x80 >> column)
            self.green_buf[row] &= ~(0x80 >> column)
        else:
            self.green_buf[row] |= (0x80 >> column)
            self.red_buf[row] |= (0x80 >> column)
        self._send_row(row)

    def clear_pixel(self, row, column):
        """
        Clear pixel.
        """
        self.green_buf[row] &= ~(0x80 >> column)
        self.red_buf[row] &= ~(0x80 >> column)
        self._send_row(row)

    def fill(self, color):
        for i in range(8):
            self.set_row_by_color(i, 0xFF, color)


