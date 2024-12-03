vietnamese_to_digit = {
    "Không": 0,
    "Một": 1,
    "hAii": 2,
    "bA": 3,
    "BốN": 4,
    "năM": 5,
    "Sấu": 6,
    "Bảy": 7,
    "TáM": 8,
    "Chứn": 9,
    "không": 0,
    "một": 1,
    "hai": 2,
    "ba": 3,
    "bốn": 4,
    "năm": 5,
    "sáu": 6,
    "bảy": 7,
    "tám": 8,
    "chín": 9,
    "Khôngg": 0,
    "Mộtt": 1,
    "hAaii": 2,
    "bbA": 3,
    "Bốnn": 4,
    "BbốN": 4,
    "nnăM": 5,
    "Sấuu": 6,
    "Bbảy": 7,
    "TámM": 8,
    "Chứnn": 9
}
# S [Một]+[bA] à=?
# Ơ [hAii]+[BốN] P=?
def solve_TangKiemNgoaiTruyen_pattern(input_string):
    parts = input_string.split()
    
    digit_words = parts[1].split("+")
    
    digit1_word = digit_words[0].strip("[]")
    digit2_word = digit_words[1].strip("[]")

    digit1 = vietnamese_to_digit[digit1_word]
    digit2 = vietnamese_to_digit[digit2_word]
    
    return str(digit1 + digit2)

# Tính: 9+hai
def solve_vl2kyuc_pattern(input_string):
    # Split the input string by "Tính: "
    parts = input_string.split(":")
    
    # The part after "Tính: "
    expression = parts[1].strip()
    
    # Split by "+" to separate the two parts
    digit_words = expression.split("+")
    
    # Process the first digit (it can be a numeric digit or a Vietnamese word)
    digit1_word = digit_words[0].strip()
    if digit1_word.isdigit():  # If it's already a digit
        digit1 = int(digit1_word)
    else:  # If it's a Vietnamese word
        digit1 = vietnamese_to_digit[digit1_word]
    
    # Process the second digit (similar to the first one)
    digit2_word = digit_words[1].strip()
    if digit2_word.isdigit():  # If it's already a digit
        digit2 = int(digit2_word)
    else:  # If it's a Vietnamese word
        digit2 = vietnamese_to_digit[digit2_word]
    
    # Return the sum of the two digits as a string
    return str(digit1 + digit2)

def recognize_pattern(input_string):
    # Check if the input has 'Tính:'
    if "TƯnh:" in input_string:
        return solve_vl2kyuc_pattern(input_string)
    else:
        return solve_TangKiemNgoaiTruyen_pattern(input_string)
