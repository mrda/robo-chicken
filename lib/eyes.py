import matrix8x8
import time

class Eye:

    def __init__(self, addr=None):
        if addr is None:
            self.d = matrix8x8.Matrix8x8()
        else:
            self.d = matrix8x8.Matrix8x8(addr=addr)
        self.empty = [0] * 8
        self.empty[0]  = int("00000000", 2)
        self.empty[1]  = int("00000000", 2)
        self.empty[2]  = int("00000000", 2)
        self.empty[3]  = int("00000000", 2)
        self.empty[4]  = int("00000000", 2)
        self.empty[5]  = int("00000000", 2)
        self.empty[6]  = int("00000000", 2)
        self.empty[7]  = int("00000000", 2)

    def eye_left_down(self):
        a = [0] * 8
        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("00000000", 2)
        a[3]  = int("00000000", 2)
        a[4]  = int("00000110", 2)
        a[5]  = int("00001111", 2)
        a[6]  = int("00001111", 2)
        a[7]  = int("00000110", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_left_up(self):
        a = [0] * 8
        a[0]  = int("00000110", 2)
        a[1]  = int("00001111", 2)
        a[2]  = int("00001111", 2)
        a[3]  = int("00000110", 2)
        a[4]  = int("00000000", 2)
        a[5]  = int("00000000", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_left_centre(self):
        a = [0] * 8
        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("00000110", 2)
        a[3]  = int("00001111", 2)
        a[4]  = int("00001111", 2)
        a[5]  = int("00000110", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_centre_down(self):
        a = [0] * 8
        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("00000000", 2)
        a[3]  = int("00000000", 2)
        a[4]  = int("00011000", 2)
        a[5]  = int("00111100", 2)
        a[6]  = int("00111100", 2)
        a[7]  = int("00011000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_centre_centre(self):
        b = [0] * 8
        b[0]  = int("00000000", 2)
        b[1]  = int("00000000", 2)
        b[2]  = int("00011000", 2)
        b[3]  = int("00111100", 2)
        b[4]  = int("00111100", 2)
        b[5]  = int("00011000", 2)
        b[6]  = int("00000000", 2)
        b[7]  = int("00000000", 2)
        self.d.green_buf = bytearray(self.empty)
        self.d.red_buf = bytearray(b)
        self.d._send_buf()

    def eye_centre_up(self):
        a = [0] * 8
        a[0]  = int("00011000", 2)
        a[1]  = int("00111100", 2)
        a[2]  = int("00111100", 2)
        a[3]  = int("00011000", 2)
        a[4]  = int("00000000", 2)
        a[5]  = int("00000000", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_right_down(self):
        a = [0] * 8
        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("00000000", 2)
        a[3]  = int("00000000", 2)
        a[4]  = int("01100000", 2)
        a[5]  = int("11110000", 2)
        a[6]  = int("11110000", 2)
        a[7]  = int("01100000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_right_centre(self):
        a = [0] * 8
        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("01100000", 2)
        a[3]  = int("11110000", 2)
        a[4]  = int("11110000", 2)
        a[5]  = int("01100000", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_right_up(self):
        a = [0] * 8
        a[0]  = int("01100000", 2)
        a[1]  = int("11110000", 2)
        a[2]  = int("11110000", 2)
        a[3]  = int("01100000", 2)
        a[4]  = int("00000000", 2)
        a[5]  = int("00000000", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()


