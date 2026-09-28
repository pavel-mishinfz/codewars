from collections import Counter


def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    counter = Counter(walk)
    return counter['n'] == counter['s'] and counter['w'] == counter['e']