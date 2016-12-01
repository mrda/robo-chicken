import simplematrix8x8

class Eye:

    EMPTY = 0
    TWO = 0b00011000
    FOUR = 0b00111100

    def __init__(self, addr=None):
        if addr is None:
            self.d = simplematrix8x8.SimpleMatrix8x8()
        else:
            self.d = simplematrix8x8.SimpleMatrix8x8(addr=addr)
        self.empty = [0] * 8

    def eye_right_centre(self):
        a = [0] * 8
        a[2]  = Eye.TWO >> 2
        a[3]  = Eye.FOUR >> 2
        a[4]  = Eye.FOUR >> 2
        a[5]  = Eye.TWO >> 2
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_centre_centre(self):
        b = [0] * 8
        b[2]  = Eye.TWO
        b[3]  = Eye.FOUR
        b[4]  = Eye.FOUR
        b[5]  = Eye.TWO
        self.d.green_buf = bytearray(b)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_centre_down(self):
        b = [0] * 8
        b[4]  = Eye.TWO
        b[5]  = Eye.FOUR
        b[6]  = Eye.FOUR
        b[7]  = Eye.TWO
        self.d.green_buf = bytearray(b)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_left_centre(self):
        a = [0] * 8
        a[2]  = Eye.TWO << 2
        a[3]  = Eye.FOUR << 2
        a[4]  = Eye.FOUR << 2
        a[5]  = Eye.TWO << 2
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()
