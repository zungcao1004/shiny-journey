import win32process
import psutil
import pygetwindow as gw
from time import sleep
from key_sender import send_keys
from captcha_handler import get_captcha_solution


def get_hwnds_from_process_name(process_name):
    """
    Retrieve a mapping of window handles (HWND) to process IDs (PID) for a specific process name.

    Args:
        process_name (str): Name of the process to search for (case insensitive).

    Returns:
        dict: A dictionary mapping HWNDs to PIDs of windows belonging to the specified process.
    """
    hwnd_pid_map = {}

    # Iterate over all running processes to find those matching the target process name
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.info["name"].lower() == process_name.lower():
                # Retrieve all windows with titles (even empty ones)
                windows = gw.getWindowsWithTitle("")
                for window in windows:
                    hwnd = window._hWnd  # Window handle
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)  # Get process ID from HWND
                    if pid == proc.info["pid"]:  # Match the PID to the process
                        hwnd_pid_map[hwnd] = pid  # Map HWND to PID
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            # Handle processes that no longer exist or can't be accessed
            continue

    return hwnd_pid_map


def monitor_and_solve_captcha(process_name):
    """
    Monitor windows belonging to the specified process and solve captchas by sending keys.

    Args:
        process_name (str): Name of the process to monitor (case insensitive).
    """
    while True:
        try:
            # Retrieve window handles and process IDs for the target process
            hwnd_pid_map = get_hwnds_from_process_name(process_name)
            if hwnd_pid_map:
                for hwnd, pid in hwnd_pid_map.items():
                    # Solve the captcha for the given process
                    captcha_solution = get_captcha_solution(pid)
                    if captcha_solution:
                        # Send the captcha solution and press 'escape' afterward
                        send_keys(hwnd, [captcha_solution, "escape"], delay=0.1)
                        print(f"Captcha solution sent to HWND {hwnd} for PID {pid}.")
                    else:
                        print(f"No valid captcha solution for PID {pid}.")
                sleep(0.1)  # Short delay before checking again
            else:
                print(f"No windows found for process '{process_name}'.")
                sleep(2)  # Wait before checking again if no windows are found
        except Exception as e:
            # Log and handle unexpected errors
            print(f"An unexpected error occurred: {e}")
            sleep(2)  # Wait before retrying to avoid rapid failures


# Example usage:
# monitor_and_solve_captcha("so2game.exe")
