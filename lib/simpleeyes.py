import simplematrix8x8

class SimpleEyes:

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
        a[2] = a[5] = SimpleEyes.TWO >> 2
        a[3] = a[4] = SimpleEyes.FOUR >> 2
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_centre_centre(self):
        b = [0] * 8
        b[2] = b[5] = SimpleEyes.TWO
        b[3] = b[4] = SimpleEyes.FOUR
        self.d.green_buf = bytearray(b)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_centre_down(self):
        b = [0] * 8
        b[4] = b[7] = SimpleEyes.TWO
        b[5] = b[6] = SimpleEyes.FOUR
        self.d.green_buf = bytearray(b)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()

    def eye_left_centre(self):
        a = [0] * 8
        a[2] = a[5] = SimpleEyes.TWO << 2
        a[3] = a[4] = SimpleEyes.FOUR << 2
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(self.empty)
        self.d._send_buf()
