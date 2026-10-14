def last_digit(n1, n2):
    if n2 == 0:
        return 1

    last_digit_base = n1 % 10
    x = 1
    last_digits = []
    while len(last_digits) < 4:
        x *= last_digit_base
        x %= 10
        last_digits.append(x)

    cycle_len = 2 if last_digits[:2] == last_digits[2:4] else 4
    idx = n2 % cycle_len - 1
    return last_digits[idx]