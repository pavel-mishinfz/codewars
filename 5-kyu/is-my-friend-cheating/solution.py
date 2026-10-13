def remov_nb(n):
    seq = list(range(1, n + 1))
    s = (n * (n + 1)) // 2

    result = []
    for x in seq:
        is_int = (s - x) % (1 + x) == 0
        y = (s - x) // (1 + x)
        if is_int and y in seq:
            result.append((x, y))
    return result
