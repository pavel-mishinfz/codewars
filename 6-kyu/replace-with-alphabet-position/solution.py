def alphabet_position(text):
    return ' '.join([str(ord(ch.lower()) - ord('a') + 1) for ch in text if ch.isalpha()])