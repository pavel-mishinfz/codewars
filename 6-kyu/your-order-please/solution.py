import re


def order(sentence):
    words = sentence.split()
    words.sort(key=lambda x: re.search(r'[0-9]', x).group())
    return ' '.join(words)