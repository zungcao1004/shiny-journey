import re
from word_processor import preprocess_word

def solve_addition_pattern(input_string):
    """
    Solve a simple addition pattern where input is like '9+hai'.

    Args:
        input_string (str): The input string containing the addition pattern.
    Returns:
        str: The sum of the two numbers as a string.
    """
    try:
        # Normalize and split input string
        input_string = input_string.lower()
        # parts = input_string.split()
        
        # # Ensure there's a '+' operator
        # if len(parts) < 2 or "+" not in parts[1]:
        #     raise ValueError("Invalid addition pattern format")

        # Extract and clean the two components
        # digit_words = parts[1].split("+")
        digit_words = input_string.split("+")
        digit1_word = digit_words[0].strip("[]")
        digit2_word = digit_words[1].strip("[]")

        # Convert words to numeric values
        digit1 = preprocess_word(digit1_word)
        digit2 = preprocess_word(digit2_word)
        
        return str(digit1 + digit2)
    except Exception as e:
        return f"Error solving addition pattern: {e}"

def solve_vl2kyuc_pattern(input_string):
    """
    Solve patterns of the form 'Tính: 9+hai' by extracting numeric and word values.

    Args:
        input_string (str): The input string containing the pattern.
    Returns:
        str: The sum of the two numbers as a string.
    """
    try:
        # Match the pattern after "Tính:"
        match = re.match(r"tưnh:\s*(\S+)\s*\+\s*(\S+)", input_string.strip().lower())
        if not match:
            raise ValueError("Invalid format for 'Tính:' pattern")

        digit1_word, digit2_word = match.groups()

        # Convert first part to number
        digit1 = int(digit1_word) if digit1_word.isdigit() else preprocess_word(digit1_word)
        
        # Convert second part to number
        digit2 = int(digit2_word) if digit2_word.isdigit() else preprocess_word(digit2_word)
        
        return str(digit1 + digit2)
    except Exception as e:
        return f"Error solving 'Tính:' pattern: {e}"

def process_escape_input(input_string):
    """
    Handle special cases like 'Chuỗi kư tự nhập vào quá Ưt!'.

    Args:
        input_string (str): The input string containing an escape scenario.
    Returns:
        list: A list of strings like ['escape', 'escape'] indicating an escape command.
    """
    if "chuỗi kư tự nhập vào quá" in input_string.lower():
        return ["escape", "escape"]
    return []

def recognize_pattern(input_string):
    """
    Recognize and solve the pattern in the input string.

    Args:
        input_string (str): The input string to analyze.
    Returns:
        str | list: The result of the recognized pattern or special case processing.
    """
    # Handle escape scenario
    escape_result = process_escape_input(input_string)
    if escape_result:
        return escape_result

    # Check for 'Tính:' pattern
    if re.match(r"tưnh:", input_string.strip().lower()):
        return solve_vl2kyuc_pattern(input_string)
    
    # Fallback to addition pattern
    return solve_addition_pattern(input_string)

# ố[TámM]+[Bbảy]z=?
# kg[Khôngg]+[bbA]?g=?
# ;g[bbA]+[nnăM]xc=?
# ?c[TámM]+[BbốN]sg=?
# "tg[MườiiBốn]+[nnăM][g=?"

# print(type(recognize_pattern("TƯnh: chƯn+0")))
# print(solve_vl2kyuc_pattern("TƯnh: chƯn+0"))

