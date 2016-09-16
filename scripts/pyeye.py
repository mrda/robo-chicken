import eyes
import ws

def choose_eye(x, y):
    x = int(x)
    y = int(y)
    e = eyes.Eye()
    if x <= 500:
        if y <=350:
            e.eye_left_up()
        else:
            e.eye_left_down()
    elif x <= 900:
        if y <=350:
            e.eye_centre_up()
        else:
            e.eye_centre_down()
    else:
        if y <=350:
            e.eye_right_up()
        else:
            e.eye_right_down()

def manage_cursor(data):
    parts = data.split('/')
    choose_eye(parts[0], parts[1])
    return "Thanks for all the fish!"

w = ws.WebServer()
w.register_url("GET", "mouse", manage_cursor)


w.start()
