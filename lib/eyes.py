import matrix8x8
import time

class Eye:

    def __init__(self):
        self.d = matrix8x8.Matrix8x8()

    def eye_left_down(self):

        #print("eye_left_down")

        a = [0] * 8
        b = [0] * 8

        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("00011111", 2)
        a[3]  = int("00111111", 2)
        a[4]  = int("00111111", 2)
        a[5]  = int("00111100", 2)
        a[6]  = int("00111000", 2)
        a[7]  = int("00111000", 2)

        b[0]  = int("00000000", 2)
        b[1]  = int("00000000", 2)
        b[2]  = int("00000000", 2)
        b[3]  = int("00001111", 2)
        b[4]  = int("00011111", 2)
        b[5]  = int("00011111", 2)
        b[6]  = int("00011111", 2)
        b[7]  = int("00011111", 2)

        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(b)
        self.d._send_buf()

    def eye_centre_down(self):
        #print("eye_centre_down")
        a = [0] * 8
        b = [0] * 8

        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("01111110", 2)
        a[3]  = int("11111111", 2)
        a[4]  = int("11111111", 2)
        a[5]  = int("11100111", 2)
        a[6]  = int("11000011", 2)
        a[7]  = int("11000011", 2)

        b[0]  = int("00000000", 2)
        b[1]  = int("00000000", 2)
        b[2]  = int("00000000", 2)
        b[3]  = int("00111100", 2)
        b[4]  = int("01111110", 2)
        b[5]  = int("01111110", 2)
        b[6]  = int("01111110", 2)
        b[7]  = int("01111110", 2)

        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(b)
        self.d._send_buf()


    def eye_right_down(self):
        #print("eye_right_down")
        a = [0] * 8
        b = [0] * 8

        a[0]  = int("00000000", 2)
        a[1]  = int("00000000", 2)
        a[2]  = int("11111000", 2)
        a[3]  = int("11111100", 2)
        a[4]  = int("11111100", 2)
        a[5]  = int("00111100", 2)
        a[6]  = int("00011100", 2)
        a[7]  = int("00011100", 2)

        b[0]  = int("00000000", 2)
        b[1]  = int("00000000", 2)
        b[2]  = int("00000000", 2)
        b[3]  = int("11110000", 2)
        b[4]  = int("11111000", 2)
        b[5]  = int("11111000", 2)
        b[6]  = int("11111000", 2)
        b[7]  = int("11111000", 2)

        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(b)
        self.d._send_buf()

    def eye_left_up(self):
        #print("eye_left_up")
        a = [0] * 8
        b = [0] * 8

        a[0]  = int("00111000", 2)
        a[1]  = int("00111000", 2)
        a[2]  = int("00111100", 2)
        a[3]  = int("00111111", 2)
        a[4]  = int("00111111", 2)
        a[5]  = int("00011111", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)

        b[0]  = int("00011111", 2)
        b[1]  = int("00011111", 2)
        b[2]  = int("00011111", 2)
        b[3]  = int("00011111", 2)
        b[4]  = int("00001111", 2)
        b[5]  = int("00000000", 2)
        b[6]  = int("00000000", 2)
        b[7]  = int("00000000", 2)
        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(b)
        self.d._send_buf()



    def eye_right_up(self):
        #print("eye_right_up")

        a = [0] * 8
        b = [0] * 8

        a[0]  = int("00011100", 2)
        a[1]  = int("00011100", 2)
        a[2]  = int("00111100", 2)
        a[3]  = int("11111100", 2)
        a[4]  = int("11111100", 2)
        a[5]  = int("11111000", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)

        b[0]  = int("11111000", 2)
        b[1]  = int("11111000", 2)
        b[2]  = int("11111000", 2)
        b[3]  = int("11111000", 2)
        b[4]  = int("11110000", 2)
        b[5]  = int("00000000", 2)
        b[6]  = int("00000000", 2)
        b[7]  = int("00000000", 2)

        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(b)
        self.d._send_buf()

    def eye_centre_up(self):
        #print("eye_center_up")
        a = [0] * 8
        b = [0] * 8

        a[0]  = int("11000011", 2)
        a[1]  = int("11000011", 2)
        a[2]  = int("11100111", 2)
        a[3]  = int("11111111", 2)
        a[4]  = int("11111111", 2)
        a[5]  = int("01111110", 2)
        a[6]  = int("00000000", 2)
        a[7]  = int("00000000", 2)

        b[0]  = int("01111110", 2)
        b[1]  = int("01111110", 2)
        b[2]  = int("01111110", 2)
        b[3]  = int("01111110", 2)
        b[4]  = int("00111100", 2)
        b[5]  = int("00000000", 2)
        b[6]  = int("00000000", 2)
        b[7]  = int("00000000", 2)

        self.d.green_buf = bytearray(a)
        self.d.red_buf = bytearray(b)
        self.d._send_buf()


#def scan():
#    d = matrix8x8.Matrix8x8()
#    delay = 0.5
#    for i in range(10):
#        _eye_right_down(d)
#        time.sleep(delay)
#        _eye_centre_down(d)
#        time.sleep(delay)
#        _eye_left_down(d)
#        time.sleep(delay)
#        _eye_centre_down(d)
#        time.sleep(delay)
#
#if __name__ == '__main__':
#    scan()

