def increment_string(string):
    if string == '' or string[-1].isalpha():
        return string + '1'

    i = len(string) - 1
    while i >= 0 and string[i].isdigit():
        i -= 1

    last_digit_idx = i + 1
    digits = [int(ch) for ch in string[last_digit_idx:]]
    digits = digits[::-1]

    j = 0
    carry = 0
    digits[0] += 1
    while j < len(digits):
        digits[j] += carry
        carry = digits[j] // 10
        digits[j] %= 10
        j += 1

    if carry > 0:
        digits.append(0)
        digits[-1] += carry

    return string[:last_digit_idx] + ''.join([str(x) for x in digits[::-1]])

# using default methods is more elegant :)
# def increment_string(string):
#     base_string = string.rstrip('0123456789')
#     tail = string[len(base_string):]
#     new_tail = 1 if tail == '' else int(tail) + 1
#     return base_string + str(new_tail).zfill(len(string) - len(base_string))