# Import necessary functions from other modules
from read_memory import (
    open_process,            # Function to open a process by its PID
    get_pointer,             # Function to get the pointer to the target address
    read_process_memory_string,  # Function to read a string from a given memory address
    close_handle,            # Function to close the handle to the process
)
from word_processor import convert_tcvn3_to_unicode  # Function to convert TCVN3 encoded text to Unicode
from captcha_solver import recognize_pattern

def get_captcha(pid):
    """
    Retrieves the CAPTCHA value from the process memory.

    Args:
        pid (int): The process ID (PID) of the target process.

    Returns:
        str or None: The CAPTCHA value converted to Unicode, or None if the CAPTCHA retrieval fails.
    """
    try:
        # Open the process with the given PID to read its memory
        process_handle = open_process(pid)
        if not process_handle:
            print(f"Failed to open process with PID {pid}.")
            return None
        
        # Define the base address and offsets for accessing the CAPTCHA value in memory
        base_address = 0x0086E5E4
        offsets = [0x4C, 0x64, 0x0]
        
        # Get the memory address where the CAPTCHA value is stored
        captcha_address = get_pointer(process_handle, base_address, offsets)
        
        # Read the CAPTCHA value (string) from the process memory
        captcha_value = read_process_memory_string(process_handle, captcha_address)
        
        # Close the process handle after reading the memory
        close_handle(process_handle)
        
        # Ensure CAPTCHA value is not empty or too short
        if captcha_value and len(captcha_value) > 0:
            return convert_tcvn3_to_unicode(captcha_value)
        else:
            # Log if CAPTCHA value is empty or invalid
            print(f"Captcha is empty or invalid for process with PID {pid}.")
            return None
    except Exception as e:
        # Log any exceptions that occur and provide the error details
        print(f"Error accessing process {pid}: {e}")
        return None

def get_captcha_solution(pid):
    try:
        captcha_value = get_captcha(pid)

        if captcha_value:
            print(f"Captcha retrieved from pid {pid}: ", captcha_value)
            try:
                result = recognize_pattern(captcha_value)
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

