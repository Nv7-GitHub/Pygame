from graphics import *

win = GraphWin("CheckText", 1400, 800)
key = win.getKey()
instructions = Text(Point(win.getWidth() / 2, 500), key)
instructions.setStyle("bold")
instructions.draw(win)
while True:
    instructions.undraw()
    key = win.getKey()
    instructions = Text(Point(win.getWidth() / 2, 500), key)
    instructions.setStyle("bold")
    instructions.draw(win)
