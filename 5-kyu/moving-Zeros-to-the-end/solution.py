def move_zeros(lst):
    if len(lst) < 2:
        return lst

    count_zeros = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            count_zeros += 1
        elif count_zeros > 0:
            lst[i - count_zeros] = lst[i]
            lst[i] = 0
    return lst

# use default tools
# def move_zeros(lst):
#     digits_without_zeros = ''.join([str(x) for x in lst if x > 0])
#     return [int(x) for x in digits_without_zeros.ljust(len(lst), '0')]