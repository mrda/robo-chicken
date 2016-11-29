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
import machine
import micropython
import ws


class Frankenbot:

    def __init__(self):
        self.r = drive.RoboDrive()

    def move(self, data):
        self.r.step(secs=int(data))
        return "Moving %s" % data

    def turn(self, data):
        if data.lower() == "left":
            self.r.turn_left()
            return "Turning Left!"
        elif data.lower() == "right":
            self.r.turn_right()
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
