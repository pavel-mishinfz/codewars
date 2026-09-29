def is_pangram(st):
    NUMBER_OF_LETTER_IN_ALPHABET = 26

    unique_chars = set(st.lower())
    unique_letters = [ch for ch in unique_chars if ch.isalpha()]
    return len(unique_letters) == NUMBER_OF_LETTER_IN_ALPHABET
    # import string
    # return set(string.ascii_lowercase).issubset(st.lower())