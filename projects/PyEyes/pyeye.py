import eyes
import ws

LEFT = 0
CENTRE = 1
RIGHT = 2
UP = 0
DOWN = 2

#TODO(mrda): Need to get these posted to us
MAX_WIDTH = 1280
MAX_HEIGHT = 800

class PyEye:

    def __init__(self):
        self.left_eye = eyes.Eye(addr=0x71)
        self.right_eye = eyes.Eye()

        self.eye_position = [[-1 for x in range(3)] for y in range(3)]
        self.eye_position[LEFT][UP] = (self.left_eye.eye_left_up, self.right_eye.eye_right_down)
        self.eye_position[LEFT][CENTRE] = (self.left_eye.eye_left_centre, self.right_eye.eye_right_centre)
        self.eye_position[LEFT][DOWN] = (self.left_eye.eye_left_down, self.right_eye.eye_right_up)
        self.eye_position[CENTRE][UP] = (self.left_eye.eye_centre_up, self.right_eye.eye_centre_down)
        self.eye_position[CENTRE][CENTRE] = (self.left_eye.eye_centre_centre, self.right_eye.eye_centre_centre)
        self.eye_position[CENTRE][DOWN] = (self.left_eye.eye_centre_down, self.right_eye.eye_centre_up)
        self.eye_position[RIGHT][UP] = (self.left_eye.eye_right_up, self.right_eye.eye_left_down)
        self.eye_position[RIGHT][CENTRE] = (self.left_eye.eye_right_centre, self.right_eye.eye_left_centre)
        self.eye_position[RIGHT][DOWN] = (self.left_eye.eye_right_down, self.right_eye.eye_left_up)

    def choose_eye(self, x, y):
        x = int(x)
        y = int(y)

        third_width = MAX_WIDTH / 3
        third_height = MAX_HEIGHT / 3

        if x <= third_width:
            width = LEFT
        elif x <= 2*third_width:
            width = CENTRE
        else:
            width = RIGHT

        if y <= third_height:
            height = UP
        elif y <= 2*third_height:
            height = CENTRE
        else:
            height = DOWN

        self.eye_position[width][height][0]()
        self.eye_position[width][height][1]()


    def manage_cursor(self, data):
        parts = data.split('/')
        self.choose_eye(parts[0], parts[1])
        return "Thanks for all the fish!"

w = ws.WebServer()
pyeye = PyEye()
w.register_url("GET", "mouse", pyeye.manage_cursor)
w.start()
