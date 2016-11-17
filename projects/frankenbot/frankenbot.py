#
# frankenbot - REST api controlled cardboard robot
#

import drive
import ws


class Frankenbot:

    def __init__(self):
        self.r = drive.RoboDrive()

    def move(self, data):
        self.r.step()
        return "Moving 1"

    def turn(self, data):
        if data.lower() == "left":
            self.r.turn_left()
            return "Turning Left!"
        elif data.lower() == "right":
            self.r.turn_right()
            return "Turning Right!"
        else:
            return "Unknown direction"

w = ws.WebServer()
f = Frankenbot()
w.register_url("PUT", "turn", f.turn)
w.register_url("PUT", "move", f.move)
w.start()
