vietnamese_to_digit = {
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
    "chứn": 9,
    "mười": 10,
    "mười một": 11,
    "mười hai": 12,
    "mười ba": 13,
    "mười bốn": 14,
    "mười năm": 15,
    "mười sáu": 16,
    "mười bảy": 17,
    "mười tám": 18,
    "mười chín": 19,
    "hai mươi": 20,
}

tcvn3_to_unicode = {
    "Aµ": "À",
    "A¸": "Á",
    "¢": "Â",
    "A·": "Ã",
    "EÌ": "È",
    "EÐ": "É",
    "£": "Ê",
    "I×": "Ì",
    "IÝ": "Í",
    "Oß": "Ò",
    "Oã": "Ó",
    "¤": "Ô",
    "Oâ": "Õ",
    "Uï": "Ù",
    "Uó": "Ú",
    "Yý": "Ý",
    "µ": "à",
    "¸": "á",
    "©": "â",
    "·": "ã",
    "Ì": "è",
    "Ð": "é",
    "ª": "ê",
    "×": "ì",
    "Ý": "í",
    "ß": "ò",
    "ã": "ó",
    "«": "ô",
    "â": "õ",
    "ï": "ù",
    "ó": "ú",
    "ý": "ý",
    "¡": "Ă",
    "¨": "ă",
    "§": "Đ",
    "®": "đ",
    "IÜ": "Ĩ",
    "Ü": "ĩ",
    "Uò": "Ũ",
    "ò": "ũ",
    "¥": "Ơ",
    "¬": "ơ",
    "¦": "Ư",
    "\xad": "ư",
    "A¹": "Ạ",
    "¹": "ạ",
    "A¶": "Ả",
    "¶": "ả",
    "¢Ê": "Ấ",
    "Ê": "ấ",
    "¢Ç": "Ầ",
    "Ç": "ầ",
    "¢È": "Ẩ",
    "È": "ẩ",
    "¢É": "Ẫ",
    "É": "ẫ",
    "¢Ë": "Ậ",
    "Ë": "ậ",
    "¡¾": "Ắ",
    "¾": "ắ",
    "¡»": "Ằ",
    "»": "ằ",
    "¡¼": "Ẳ",
    "¼": "ẳ",
    "¡½": "Ẵ",
    "½": "ẵ",
    "¡Æ": "Ặ",
    "Æ": "ặ",
    "EÑ": "Ẹ",
    "Ñ": "ẹ",
    "EÎ": "Ẻ",
    "Î": "ẻ",
    "EÏ": "Ẽ",
    "Ï": "ẽ",
    "£Õ": "Ế",
    "Õ": "ế",
    "£Ò": "Ề",
    "Ò": "ề",
    "£Ó": "Ể",
    "Ó": "ể",
    "£Ô": "Ễ",
    "Ô": "ễ",
    "£Ö": "Ệ",
    "Ö": "ệ",
    "IØ": "Ỉ",
    "Ø": "ỉ",
    "IÞ": "Ị",
    "Þ": "ị",
    "Oä": "Ọ",
    "ä": "ọ",
    "Oá": "Ỏ",
    "á": "ỏ",
    "¤è": "Ố",
    "è": "ố",
    "¤å": "Ồ",
    "å": "ồ",
    "¤æ": "Ổ",
    "æ": "ổ",
    "¤ç": "Ỗ",
    "ç": "ỗ",
    "¤é": "Ộ",
    "é": "ộ",
    "¥í": "Ớ",
    "í": "ớ",
    "¥ê": "Ờ",
    "ê": "ờ",
    "¥ë": "Ở",
    "ë": "ở",
    "¥ì": "Ỡ",
    "ì": "ỡ",
    "¥î": "Ợ",
    "î": "ợ",
    "Uô": "Ụ",
    "ô": "ụ",
    "Uñ": "Ủ",
    "ñ": "ủ",
    "¦ø": "Ứ",
    "ø": "ứ",
    "¦õ": "Ừ",
    "õ": "ừ",
    "¦ö": "Ử",
    "ö": "ử",
    "¦÷": "Ữ",
    "÷": "ữ",
    "¦ù": "Ự",
    "ù": "ự",
    "Yú": "Ỳ",
    "ú": "ỳ",
    "Yþ": "Ỵ",
    "þ": "ỵ",
    "Yû": "Ỷ",
    "û": "ỷ",
    "Yü": "Ỹ",
    "ü": "ỹ",
}


# Function to convert TCVN3 encoded text to Unicode
def convert_tcvn3_to_unicode(tcvn3_text: str) -> str:
    """
    Converts TCVN3 encoded text to Unicode by mapping each character to its Unicode equivalent.
    
    Args:
        tcvn3_text (str): The TCVN3 encoded string to be converted.

    Returns:
        str: The converted Unicode string.
    """
    # Create the Unicode string by mapping each character using a predefined dictionary
    return "".join([tcvn3_to_unicode.get(char, char) for char in tcvn3_text])


# Function to calculate the similarity score between two words
def calculate_similarity(word1: str, word2: str) -> float:
    """
    Calculates the similarity score between two words based on their characters.

    The similarity score is based on the number of matching characters between the two words,
    normalized by the average length of both words.

    Args:
        word1 (str): The first word to compare.
        word2 (str): The second word to compare.

    Returns:
        float: A normalized similarity score between 0 and 1, where 1 means identical words.
    """
    word1, word2 = word1.lower(), word2.lower()
    

    set1, set2 = set(word1), set(word2)
    matches = len(set1 & set2)  # Intersection of character sets
    normalized_score = matches / ((len(word1) + len(word2)) / 2)
    
    return normalized_score


# Function to normalize a Vietnamese word to its closest valid match
def normalize_vietnamese_word(input_word: str) -> str:
    """
    Normalizes the input Vietnamese word to its closest valid word based on similarity.

    This function compares the input word with a set of valid words (e.g., Vietnamese-to-digit map)
    and selects the best match based on the highest similarity score.

    Args:
        input_word (str): The Vietnamese word to be normalized.

    Returns:
        str: The best-matching valid Vietnamese word.
    """
    valid_words = vietnamese_to_digit.keys()
    best_match = None
    highest_similarity = 0

    for valid_word in valid_words:
        similarity = calculate_similarity(input_word, valid_word)
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = valid_word

    if best_match is None:
        print(f"No valid match found for word: {input_word}")
    
    return best_match


# Example function to preprocess a word before digit conversion
def preprocess_word(input_word: str) -> str:
    """
    Preprocesses the input word by normalizing it to the closest valid Vietnamese word,
    and then converts it to its corresponding digit using the vietnamese_to_digit mapping.

    Args:
        input_word (str): The Vietnamese word to preprocess.

    Returns:
        str: The corresponding digit (as a string) for the normalized word, or None if no match.
    """
    normalized_word = normalize_vietnamese_word(input_word)
    
    # Return corresponding digit or handle case where no match is found
    if normalized_word:
        return vietnamese_to_digit.get(normalized_word)
    else:
        print(f"Cannot find a corresponding digit for the word: {input_word}")
        return None


# test_inputs = ["Mườii", "MườiiMột", "MườiHaii", "MườiiBa", "MườiiBốn", "MườiiNăm", "MườiSáuu", "MườiBbảy", "HhaiMươi"]
# test_input = "chƯn"
# print(preprocess_word(test_input))
# for test_input in test_inputs:
#     print(f"Input: {test_input}")
#     digit = preprocess_word(test_input)
#     print(f"Converted Digit: {digit}")
#     print("-" * 30)