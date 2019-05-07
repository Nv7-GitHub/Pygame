from graphics import *
win = GraphWin("Drive", 1400, 800)

usernames = str(open("Username.txt").read()).split("\n")
passwords = str(open("Password.txt").read()).split("\n")
files = str(open("Files.txt").read()).split("\n")
wfile = open("Files.txt", "w")
wpassword = open("Password.txt", "a+")
wusername = open("Username.txt", "a+")
username = ""
password = ""

# Username
usernamemessage = Text(Point(win.getWidth() / 2, 100), "Username:")
usernameentry = Entry(Point(win.getWidth() / 2, 200), 100)
usernamemessage.draw(win)
usernameentry.draw(win)

# Password
passwordmessage = Text(Point(win.getWidth() / 2, 300), "Password:")
passwordentry = Entry(Point(win.getWidth() / 2, 400), 100)
passwordmessage.draw(win)
passwordentry.draw(win)

# Instructions
instructions = Text(Point(win.getWidth() / 2, 500),
                    "Press ENTER to signal you are done, press control for a new account")
instructions.setStyle("bold")
instructions.draw(win)

# Wait until ENTER pressed
key_pressed = win.getKey()
while not (key_pressed == "Return" or key_pressed == "Control_L"):
    key_pressed = win.getKey()

if key_pressed == "Return":
    username = usernameentry.getText()
    password = passwordentry.getText()
else:
    usernameentry.undraw()
    usernamemessage.undraw()
    passwordentry.undraw()
    passwordmessage.undraw()
    instructions.undraw()

    usernamemessage = Text(Point(win.getWidth() / 2, 100), "New Username:")
    passwordmessage = Text(Point(win.getWidth() / 2, 300), "New Password:")
    usernameentry.draw(win)
    passwordentry.draw(win)
    usernamemessage.draw(win)
    passwordmessage.draw(win)
    instructions = Text(Point(win.getWidth() / 2, 500), "Press ENTER to signal you are done entering your "
                                                        "new username")
    instructions.setStyle("bold")
    instructions.draw(win)
    key_pressed = win.getKey()
    while not (key_pressed == "Return"):
        key_pressed = win.getKey()

    username = usernameentry.getText()
    password = passwordentry.getText()

    wfile.write("\n")
    wpassword.write(f"\n{password}")
    wusername.write(f"\n{username}")

i = 0
file = "Error404: File not found"
usernameentry.undraw()
usernamemessage.undraw()
passwordentry.undraw()
passwordmessage.undraw()
instructions.undraw()
while i < len(usernames):
    if usernames[i] == username and passwords[i] == password:
        file = files[i]

    i += 1

file = Text(Point(win.getWidth() / 2, 30), f"Your File:\n\n{file}")
file.draw(win)
instructions = Text(Point(win.getWidth() / 2, 200),
                    "Press control to edit your file, press enter to close the window")
instructions.setStyle("bold")
instructions.draw(win)
key_pressed = win.getKey()
while not(key_pressed == "Control_L" or key_pressed == "Return"):
    key_pressed = win.getKey()

if key_pressed == "Control_L":
    textmessage = Text(Point(win.getWidth() / 2, 100), "New Text For File:")
    textentry = Entry(Point(win.getWidth() / 2, 200), 100)
    instructions = Text(Point(win.getWidth() / 2, 300), "Press ENTER to signal you are done.")
    instructions.setStyle("bold")
    instructions.undraw()
    file.undraw()
    instructions.draw(win)
    textmessage.draw(win)
    textentry.draw(win)
    while not (key_pressed == "Return"):
        key_pressed = win.getKey()

    files[i - 1] = textentry.getText()

    with open('Files.txt', 'w') as file:
        file.write('\n'.join(files))
