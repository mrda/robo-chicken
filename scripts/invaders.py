import matrix8x8
import time

def _invader_a(d):
    a = [0] * 8
    b = [0] * 8

    a[0]  = int("00100100", 2)
    a[1]  = int("00011000", 2)
    a[2]  = int("00111100", 2)
    a[3]  = int("01011010", 2)
    a[4]  = int("11111111", 2)
    a[5]  = int("10111101", 2)
    a[6]  = int("10100101", 2)
    a[7]  = int("00111100", 2)

    b[0]  = int("00100100", 2)
    b[1]  = int("00011000", 2)
    b[2]  = int("00000000", 2)
    b[3]  = int("00100100", 2)
    b[4]  = int("10000001", 2)
    b[5]  = int("10000001", 2)
    b[6]  = int("10100101", 2)
    b[7]  = int("00111100", 2)

    d.green_buf = bytearray(a)
    d.red_buf = bytearray(b)
    d._send_buf()

def _invader_b(d):
    a = [0] * 8
    b = [0] * 8

    a[0]  = int("00100100", 2)
    a[1]  = int("10011001", 2)
    a[2]  = int("10111101", 2)
    a[3]  = int("11011011", 2)
    a[4]  = int("11111111", 2)
    a[5]  = int("00111100", 2)
    a[6]  = int("00100100", 2)
    a[7]  = int("01000010", 2)

    b[0]  = int("00100100", 2)
    b[1]  = int("10011001", 2)
    b[2]  = int("10000001", 2)
    b[3]  = int("10100101", 2)
    b[4]  = int("10000001", 2)
    b[5]  = int("00000000", 2)
    b[6]  = int("00100100", 2)
    b[7]  = int("01000010", 2)

    d.green_buf = bytearray(a)
    d.red_buf = bytearray(b)
    d._send_buf()

def run():
    d = matrix8x8.Matrix8x8()
    for i in range(10):
        _invader_a(d)
        time.sleep(0.5)
        _invader_b(d)
        time.sleep(0.5)
    d.set_blinking(1)
    time.sleep(6)
    d.clear()

run()
