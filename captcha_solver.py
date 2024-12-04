import re
from word_processor import preprocess_word

# Solve addition pattern (example: "9+hai")
def solve_addition_pattern(input_string):
    # Normalize input by converting to lowercase and splitting by spaces
    input_string = input_string.lower()
    parts = input_string.split()
    
    # Split the second part into digit words (e.g. "9" and "hai")
    digit_words = parts[1].split("+")
    
    # Process both digit words
    digit1_word = digit_words[0].strip("[]")
    digit2_word = digit_words[1].strip("[]")

    # Convert words to numeric values
    digit1 = preprocess_word(digit1_word)
    digit2 = preprocess_word(digit2_word)
    
    return str(digit1 + digit2)

# Solve pattern for expressions like "Tính: 9+hai"
def solve_vl2kyuc_pattern(input_string):
    # Use regular expression to extract the expression after "Tính: "
    match = re.match(r"tính:\s*(\S+)\s*\+\s*(\S+)", input_string.strip().lower())
    if match:
        digit1_word, digit2_word = match.groups()
        
        # Process the first digit (numeric or Vietnamese word)
        if digit1_word.isdigit():  # If it's already a digit
            digit1 = int(digit1_word)
        else:  # If it's a Vietnamese word
            digit1 = preprocess_word(digit1_word)
        
        # Process the second digit similarly
        if digit2_word.isdigit():
            digit2 = int(digit2_word)
        else:
            digit2 = preprocess_word(digit2_word)
        
        # Return the sum as a string
        return str(digit1 + digit2)
    else:
        raise ValueError("Invalid input format")

# Main function to recognize and solve the pattern
def recognize_pattern(input_string):
    # Check for 'Tính:' in the input string using regex for better matching
    if re.match(r"tính:", input_string.strip().lower()):
        return solve_vl2kyuc_pattern(input_string)
    else:
        return solve_addition_pattern(input_string)
