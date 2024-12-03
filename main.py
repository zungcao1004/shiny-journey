import psutil
import os
import sys
import ctypes
import pygetwindow as gw
import win32api, win32process, win32con  # type: ignore
from captcha_solver import recognize_pattern
from read_write_memory import ReadWriteMemory
from tcvn3_to_unicode import TCVN3_to_unicode
from time import sleep

# Initialize the ReadWriteMemory instance
rwm = ReadWriteMemory()

# Get HWNDs associated with a given process name
def get_hwnds_from_process_name(process_name):
    hwnd_pid_map = {}

    # Iterate over all running processes to find matching ones
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                # List all windows for this process
                windows = gw.getWindowsWithTitle('')
                for window in windows:
                    hwnd = window._hWnd
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    if pid == proc.info['pid']:
                        hwnd_pid_map[hwnd] = pid  # Map HWND to PID in the dictionary
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue  # Handle processes that terminate or can't be accessed
    
    return hwnd_pid_map

# Send keystrokes to a window identified by its HWND
def send_keys(hwnd, key):
    try:
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, ord(str(key)), 0)
        sleep(0.2)
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x0D, 0)
    except Exception as e:
        print(f"Error sending keys: {e}")

# Retrieve captcha from process memory and solve it
def solve_captcha_from_process(pid):
    try:
        process = rwm.get_process_by_id(pid)
        process.open()

        captcha_pointer = process.get_pointer(0x0086E5E4, offsets=[0x4c, 0x64, 0x0])
        captcha = process.read_string(captcha_pointer)

        if captcha:
            print(f"Captcha retrieved from pid {pid}: ", TCVN3_to_unicode(captcha))
            try:
                result = recognize_pattern(TCVN3_to_unicode(captcha))
                if result:
                    print(f"Captcha solved for pid {pid}: {result}")
                    return result
                else:
                    print(f"Captcha solving failed for pid {pid}.")
                    return None
            except Exception as e:
                print(f"Error solving captcha for pid {pid}: {e}")
                return None
        else:
            print(f"Failed to retrieve CAPTCHA or CAPTCHA is empty from pid {pid}.")
            return None
    except Exception as e:
        print(f"Error accessing process {pid}: {e}")
        return None

# Main procedure to monitor and interact with the process
def main():
    process_name = "so2game.exe"
    while True:
        try:
            hwnd_pid_map = get_hwnds_from_process_name(process_name)
            if hwnd_pid_map:
                for hwnd, pid in hwnd_pid_map.items():
                    # Ensure the process is still running before accessing it
                    captcha_result = solve_captcha_from_process(pid)
                    if captcha_result:
                        send_keys(hwnd, captcha_result)
                        print()  # Empty line after sending keys
                    else:
                        print(f"No valid captcha solution for pid {pid}.")
                #sleep(2)  # Delay before checking again
                sleep(0.01)
            else:
                print(f"No windows found for process {process_name}.")
                sleep(2)  # Wait before checking again if no windows are found
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sleep(2)  # Wait before retrying in case of an error


def temp_main():
    process_name = "so2game.exe"
    while True:
        try:
            hwnd_pid_map = get_hwnds_from_process_name(process_name)
            if hwnd_pid_map:
                for hwnd, pid in hwnd_pid_map.items():
                    # Ensure the process is still running before accessing it
                    captcha_result = solve_captcha_from_process(pid)
                    if captcha_result:
                        print(captcha_result)
                    else:
                        print(f"No valid captcha solution for pid {pid}.")
                    sleep(2)
            else:
                print(f"No windows found for process {process_name}.")
                sleep(2)  # Wait before checking again if no windows are found
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sleep(2)  # Wait before retrying in case of an error

main()
                