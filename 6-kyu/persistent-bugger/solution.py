from functools import reduce


def persistence(n):
    multiplication = 0
    while n > 9:
        n = reduce(lambda x, y: x * y, map(int, str(n))) # or use mul from operator
        multiplication += 1
    return multiplication