def lcs(x, y):
    max_subsequence = ''
    j, k = 0, 0
    len_x = len(x)
    for ci in y:
        k = j
        while k < len_x:
            if x[k] == ci:
                max_subsequence += ci
                j = k + 1
                break
            k += 1
    return max_subsequence