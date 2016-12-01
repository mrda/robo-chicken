#
# frankenbot - REST api controlled cardboard robot
#
# Here's some usage:
#
# curl -i -X PUT http://192.168.0.128:8080/turn/left
# curl -i -X PUT http://192.168.0.128:8080/turn/right
# curl -i -X PUT http://192.168.0.128:8080/move/10

import beep
import drive
import eyes
import machine
import ws


class Frankenbot:

    def __init__(self):
        # Note(mrda): The 8 Channel PWM featherwing board
        # (https://www.adafruit.com/products/2928) uses I2C 0x70
        # as a broadcast address, so I need to change the addresses
        # that the bicolour 8x8 matrices use
        # (https://learn.adafruit.com/adafruit-led-backpack/bi-color-8x8-matrix)
        # You can see how to do that here:
        # https://learn.adafruit.com/adafruit-led-backpack/changing-i2c-address
        self.r = drive.RoboDrive()
        self.left_eye = eyes.Eye(addr=0x71)
        self.right_eye = eyes.Eye(addr=0x72)
        self.left_eye.eye_centre_centre()
        self.right_eye.eye_centre_centre()

    def move(self, data):
        self.left_eye.eye_centre_down()
        self.right_eye.eye_centre_down()
        self.r.step(secs=int(data))
        self.left_eye.eye_centre_centre()
        self.right_eye.eye_centre_centre()
        return "Moving %s" % data

    def turn(self, data):
        if data.lower() == "left":
            self.left_eye.eye_left_centre()
            self.right_eye.eye_left_centre()
            self.r.turn_left()
            self.left_eye.eye_centre_centre()
            self.right_eye.eye_centre_centre()
            return "Turning Left!"
        elif data.lower() == "right":
            self.left_eye.eye_right_centre()
            self.right_eye.eye_right_centre()
            self.r.turn_right()
            self.left_eye.eye_centre_centre()
            self.right_eye.eye_centre_centre()
            return "Turning Right!"
        else:
            return "Unknown direction"

    def status(self, data):
        s = "I'm " + str(machine.unique_id()) + "\n"
        return s

    def do_beep(self, data):
        beep.play_notes(data)
        return "I like music!"


w = ws.WebServer()
f = Frankenbot()
w.register_url("PUT", "turn", f.turn)
w.register_url("PUT", "move", f.move)
w.register_url("PUT", "beep", f.do_beep)
w.register_url("GET", "status", f.status)

beep.play_mockingjay()

w.start()
