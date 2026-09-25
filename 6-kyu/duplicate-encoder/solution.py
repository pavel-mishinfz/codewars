from collections import Counter


def duplicate_encode(word):
    word_lower_case = word.lower()
    counter = Counter(word_lower_case)

    encode_str = ''
    for ch in word_lower_case:
        encode_str += ')' if counter[ch] > 1 else '('
    return encode_str