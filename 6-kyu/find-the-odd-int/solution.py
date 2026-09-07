from collections import Counter


def find_it(seq):
    counter = Counter(seq)
    for num, count in counter.items():
        if count % 2 != 0:
            return num
    return None
