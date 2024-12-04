import win32process
import psutil
import pygetwindow as gw
from time import sleep
from key_sender import send_key
from captcha_handler import get_captcha_solution


def get_hwnds_from_process_name(process_name):
    hwnd_pid_map = {}

    # Iterate over all running processes to find matching ones
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if proc.info["name"].lower() == process_name.lower():
                # List all windows for this process
                windows = gw.getWindowsWithTitle("")
                for window in windows:
                    hwnd = window._hWnd
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    if pid == proc.info["pid"]:
                        hwnd_pid_map[hwnd] = pid  # Map HWND to PID in the dictionary
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue  # Handle processes that terminate or can't be accessed

    return hwnd_pid_map


def monitor_and_solve_captcha(process_name):
    while True:
        try:
            hwnd_pid_map = get_hwnds_from_process_name(process_name)
            if hwnd_pid_map:
                for hwnd, pid in hwnd_pid_map.items():
                    # Ensure the process is still running before accessing it
                    captcha_solution = get_captcha_solution(pid)
                    if captcha_solution:
                        send_key(hwnd, captcha_solution)
                        # send_key(hwnd, "escape")
                        print()  # Empty line after sending keys
                    else:
                        print(f"No valid captcha solution for pid {pid}.")
                # sleep(2)  # Delay before checking again
                sleep(0.1)
            else:
                print(f"No windows found for process {process_name}.")
                sleep(2)  # Wait before checking again if no windows are found
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sleep(2)  # Wait before retrying in case of an error
