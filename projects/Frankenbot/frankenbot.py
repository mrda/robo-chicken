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
    SOUND = True
    EYES = True

    def __init__(self):
        if Frankenbot.SOUND:
            import beep

        if Frankenbot.MOVE:
            import drive

        if Frankenbot.EYES:
            import frankeneyes

        print ("Sound: ", Frankenbot.SOUND)
        print ("Move: ", Frankenbot.MOVE)
        print ("Eyes: ", Frankenbot.EYES)

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
        if Frankenbot.SOUND:
            self.b = beep.Beep()

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
        self.b.play_notes(data)
        return "I like music!"

    def do_mockingjay(self, data):
        self.b.play_mockingjay(data)
        return "Go Katniss!"

    def start(self):
        w = ws.WebServer()
        w.register_url("GET", "status", self.status)
        if Frankenbot.MOVE:
            w.register_url("PUT", "turn", self.turn)
            w.register_url("PUT", "move", self.move)
        w.register_url("PUT", "sound", self.do_beep)
        w.register_url("PUT", "mockingjay", self.do_mockingjay)
        w.start()
