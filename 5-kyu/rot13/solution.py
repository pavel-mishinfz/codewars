import string


def rot13(message):
    encode_msg = ''
    for ch in message:
        if ch in string.ascii_letters:
            if ch.islower():
                new_letter_idx = (ord(ch) - ord('a') + 13) % 26
                encode_msg += string.ascii_lowercase[new_letter_idx]
            if ch.isupper():
                new_letter_idx = (ord(ch) - ord('A') + 13) % 26
                encode_msg += string.ascii_uppercase[new_letter_idx]
        else:
            encode_msg += ch
    return encode_msg