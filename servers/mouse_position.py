#!/usr/bin/env python
#
# mouse_position.py - Post the current mouse position to a REST API running
#                     on a Micropython-based ESP8266
#

from Tkinter import *
import socket

root = Tk()
root.attributes('-alpha', 0.1)

maxW = root.winfo_screenwidth()
maxH = root.winfo_screenheight()
x = 0
y = 0

DELAY = 250 # microseconds
HOST = "192.168.0.127"
PORT = 8080

root.geometry("{0}x{1}+0+0".format(maxW, maxH))

print("Screen size is: width=%s height=%s" % (maxW, maxH))

# Bind the left-mouse button
#def button_click_event(event):
#    print "clicked at: ", event.x, "and: ", event.y
#root.bind("<Button-1>", button_click_event)

# Bind the <ESC> key
def exit_event(event):
    root.destroy()
root.bind("<Escape>", exit)

# Bind mouse movement
def mouse_move_event(event):
    global x, y, maxW, maxH
    x, y = event.x, event.y
    if x < 0:
        x = 0
    if x > maxW:
        x = maxW
    if y < 0:
        y = 0
    if y > maxH:
        y = maxH
root.bind("<Motion>", mouse_move_event)

def timer_event():
    global x, y
    global root
    print format_data(x, y)
    send_data(HOST, PORT, format_data(x, y))
    root.after(DELAY, timer_event)
root.after(DELAY, timer_event)

def format_data(x, y):
    return "PUT /mouse/%d/%d" % (x, y)

def send_data(host, port, data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(data)
    s.close()

root.mainloop()
