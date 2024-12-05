import time
import win32api
import win32con

def send_key(hwnd, key, delay=0.0):
    """
    Sends a single key press to the specified window.

    Args:
        hwnd (int): Handle to the window where the key should be sent.
        key (str): The key to send. Can be a single character or a special key name (e.g., "enter", "space").
        delay (float): Optional delay (in seconds) between key press and release for realistic timing.

    Raises:
        ValueError: If the key is not a valid string or unsupported special key.
    """
    try:
        # Determine the virtual key code based on the input key
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
        
        # Optional delay for more realistic key press behavior
        if delay > 0:
            time.sleep(delay)
        
        # Send the key up event (simulate releasing the key)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, key_code, 0)

    except Exception as e:
        # Log the error for debugging
        print(f"Error sending key '{key}' to hwnd {hwnd}: {e}")


def send_keys(hwnd, keys, delay=0.0):
    """
    Sends a sequence of keys to the specified window.

    Args:
        hwnd (int): Handle to the window where the keys should be sent.
        keys (list): A list of keys to send. Each key can be a single character or a special key name.
        delay (float): Optional delay (in seconds) between consecutive key presses.

    Raises:
        ValueError: If any key in the sequence is invalid or unsupported.
    """
    try:
        # Iterate over each key in the sequence
        for key in keys:
            send_key(hwnd, key, delay)  # Send each key individually
    except Exception as e:
        # Log any error that occurs during the sequence
        print(f"Error sending keys {keys} to hwnd {hwnd}: {e}")
