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
    "Chứn": 9
}

def solve_TangKiemNgoaiTruyen_pattern(input_string):
    parts = input_string.split()
    
    digit_words = parts[1].split("+")
    
    digit1_word = digit_words[0].strip("[]")
    digit2_word = digit_words[1].strip("[]")

    digit1 = vietnamese_to_digit[digit1_word]
    digit2 = vietnamese_to_digit[digit2_word]
    
    return str(digit1 + digit2)