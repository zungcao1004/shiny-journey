import ctypes

PROCESS_ALL_ACCESS = 0x1F0FFF

kernel32 = ctypes.windll.kernel32


def open_process(pid):
    """
    Open a process by its process ID (PID) with all access rights.

    Parameters:
    pid (int): The process ID of the target process.

    Returns:
    HANDLE: A handle to the opened process.

    Raises:
    ctypes.WinError: If the process cannot be opened.
    """
    handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    if not handle:
        raise ctypes.WinError(ctypes.get_last_error())
    return handle


def get_pointer(handle, base_address, offsets):
    """
    Traverse the memory addresses using base address and offsets to obtain the final pointer.

    Parameters:
    handle (HANDLE): The handle to the process.
    base_address (int): The starting address in the target process memory.
    offsets (list of int): A list of offsets to navigate through memory.

    Returns:
    int: The final address after applying all offsets.

    If no offsets are provided, returns the base address itself.
    """
    temp_address = read_process_memory_int(handle, base_address)
    if not offsets:
        return base_address
    else:
        for offset in offsets:
            # Navigate through memory by adding the offset to the current address
            pointer = temp_address + offset
            temp_address = read_process_memory_int(handle, pointer)
        return pointer


def read_process_memory_int(handle, address):
    """
    Read an integer (4 bytes) from a specified address in the target process's memory.

    Parameters:
    handle (HANDLE): The handle to the process.
    address (int): The address in the target process memory from which to read.

    Returns:
    int: The integer value read from memory.

    Raises:
    Exception: If memory cannot be read.
    """
    # Create a buffer to hold the read data (4 bytes for an integer)
    buffer = ctypes.c_uint()

    # Create a pointer to the buffer where the data will be stored
    p_buffer = ctypes.byref(buffer)

    # Size of the buffer (4 bytes for ctypes.c_uint)
    n_size = ctypes.sizeof(buffer)

    # Variable to store the number of bytes actually read
    p_number_of_bytes_read = ctypes.c_ulong(0)

    # Call ReadProcessMemory to read the memory
    success = kernel32.ReadProcessMemory(
        handle, address, p_buffer, n_size, ctypes.byref(p_number_of_bytes_read)
    )
    if not success:
        raise Exception(f"Failed to read memory at address {hex(address)}")

    # Return the value read from the memory (stored in buffer)
    return buffer.value


def read_process_memory_string(handle, address, max_length=256, encoding="cp1258"):
    """
    Read a string (null-terminated) from a specified address in the target process's memory.

    Parameters:
    handle (HANDLE): The handle to the process.
    address (int): The address in the target process memory from which to read.
    max_length (int): The maximum length of the string to read.
    encoding (str): The encoding format for decoding the bytes (default is 'cp1258').

    Returns:
    str: The string value read from memory.

    Raises:
    Exception: If the memory read operation fails.
    """
    # Create a buffer to store the string
    buffer = ctypes.create_string_buffer(max_length)

    # Pointer to the buffer
    p_buffer = ctypes.byref(buffer)

    # Size of the buffer (number of bytes to read)
    n_size = max_length

    # Variable to store the number of bytes actually read
    p_number_of_bytes_read = ctypes.c_ulong(0)

    # Read memory from the process
    success = ctypes.windll.kernel32.ReadProcessMemory(
        handle, address, p_buffer, n_size, ctypes.byref(p_number_of_bytes_read)
    )

    if success:
        # Decode the buffer value as a string, stop at null byte
        decoded_string = buffer.value.decode(encoding).split("\0", 1)[0]
        return decoded_string
    else:
        raise Exception(f"Failed to read string from address {hex(address)}")


def close_handle(handle):
    """
    Close a process handle to release resources.

    Parameters:
    handle (HANDLE): The handle to the opened process.

    Raises:
    ctypes.WinError: If the handle cannot be closed.
    """
    success = kernel32.CloseHandle(handle)
    if not success:
        raise ctypes.WinError(ctypes.get_last_error())
