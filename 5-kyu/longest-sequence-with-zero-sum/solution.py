def max_zero_sequence(arr):
    prefix_sum = [0]
    for x in arr:
        prefix_sum.append(prefix_sum[-1] + x)

    d = {}
    start = end = 0
    for i in range(len(prefix_sum)):
        item = prefix_sum[i]
        if item not in d:
            d[item] = i
        else:
            if i - d[item] >= end - start: # use > to complete the tests on Codewars
                start, end = d[item], i
    return arr[start:end]