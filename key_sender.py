import time
import win32api, win32con

# Function to send a single key press to the specified window
def send_key(hwnd, key, delay=0.0):
    try:
        # Check if the key is a single character
        if isinstance(key, str) and len(key) == 1:  # Single-character key
            key_code = ord(key)  # Convert the character to its ASCII value
        elif isinstance(key, str):  # Handle special keys by name
            # Mapping of special keys to their virtual key codes
            special_keys = {
                "enter": win32con.VK_RETURN,
                "escape": win32con.VK_ESCAPE,
                "tab": win32con.VK_TAB,
                "space": win32con.VK_SPACE,
                "backspace": win32con.VK_BACK,
                "shift": win32con.VK_SHIFT,
                "ctrl": win32con.VK_CONTROL,
                "alt": win32con.VK_MENU,
                "up": win32con.VK_UP,
                "down": win32con.VK_DOWN,
                "left": win32con.VK_LEFT,
                "right": win32con.VK_RIGHT,
                # Add more special keys as needed
            }
            # Retrieve the virtual key code for the special key
            key_code = special_keys.get(key.lower())
            if key_code is None:
                raise ValueError(f"Unsupported special key: {key}")  # Raise an error if the key is not found
        else:
            # Raise an error if the provided key is not a valid string
            raise ValueError(f"Invalid key format: {key}")

        # Send the key down event (simulate pressing the key)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, key_code, 0)
        
        # If a delay is specified, wait for the specified time to simulate realistic key press timing
        if delay > 0:
            time.sleep(delay)
        
        # Send the key up event (simulate releasing the key)
        # win32api.PostMessage(hwnd, win32con.WM_KEYUP, key_code, 0)

    except Exception as e:
        # Catch and print any error that occurs during key sending
        print(f"Error sending key {key}: {e}")

# Function to send a sequence of keys to the specified window
def send_keys(hwnd, keys, delay=0.0):
    # Iterate over each key in the provided sequence
    for key in keys:
        send_key(hwnd, key, delay)  # Call send_key for each key with the optional delay
