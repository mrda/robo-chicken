#
# frankenbot - REST api controlled cardboard robot
#
# Here's some usage:
#
# curl -i -X PUT http://192.168.0.128:8080/turn/left
# curl -i -X PUT http://192.168.0.128:8080/turn/right
# curl -i -X PUT http://192.168.0.128:8080/move/10

import machine
import ws


class Frankenbot:
    MOVE = True
    SOUND = False
    EYES = True

    def __init__(self):
        if Frankenbot.SOUND:
            import beep

        if Frankenbot.MOVE:
            import drive

        if Frankenbot.EYES:
            import frankeneyes

        # Note(mrda): The 8 Channel PWM featherwing board
        # (https://www.adafruit.com/products/2928) uses I2C 0x70
        # as a broadcast address, so I need to change the addresses
        # that the bicolour 8x8 matrices use
        # (https://learn.adafruit.com/adafruit-led-backpack/bi-color-8x8-matrix)
        # You can see how to do that here:
        # https://learn.adafruit.com/adafruit-led-backpack/changing-i2c-address
        if Frankenbot.MOVE:
            self.r = drive.RoboDrive()
        if Frankenbot.EYES:
            self.eyes = frankeneyes.FrankenEyes()

    def move(self, data):
        if Frankenbot.EYES:
            self.eyes.down()
        if Frankenbot.MOVE:
            self.r.step(secs=int(data))
        if Frankenbot.EYES:
            self.eyes.centre()
        return "Moving %s" % data

    def turn(self, data):
        if data.lower() == "left":
            if Frankenbot.EYES:
                self.eyes.left()
            if Frankenbot.MOVE:
                self.r.turn_left()
            if Frankenbot.EYES:
                self.eyes.centre()
            return "Turning Left!"
        elif data.lower() == "right":
            if Frankenbot.EYES:
                self.eyes.right()
            if Frankenbot.MOVE:
                self.r.turn_right()
            if Frankenbot.EYES:
                self.eyes.centre()
            return "Turning Right!"
        else:
            return "Unknown direction"

    def status(self, data):
        s = "I'm " + str(machine.unique_id()) + "\n"
        return s

    def do_beep(self, data):
        if Frankenbot.SOUND:
            beep.play_notes(data)
        return "I like music!"

    def do_mockingjay(self, data):
        if Frankenbot.SOUND:
            beep.play_mockingjay(data)
        return "Go Katniss!"


w = ws.WebServer()
f = Frankenbot()
w.register_url("GET", "status", f.status)
w.register_url("PUT", "turn", f.turn)
w.register_url("PUT", "move", f.move)
w.register_url("PUT", "beep", f.do_beep)
w.register_url("PUT", "mockingjay", f.do_mockingjay)

w.start()
