def sum_pairs(ints, s):
    d = {}
    for x in ints:
        if d.get(s - x) is not None:
            return [s - x, x]
        d[x] = x
    return None