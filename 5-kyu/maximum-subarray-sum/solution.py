def max_sequence(arr):
    if len(arr) == 0 or not any(x >= 0 for x in arr):
        return 0

    prefix_sum = [0]
    for x in arr:
        prefix_sum.append(prefix_sum[-1] + x)

    min_prefix_sum = 0
    max_sum_subarr = 0
    for curr_prefix_sum in prefix_sum:
        curr_sum_subarr = curr_prefix_sum - min_prefix_sum

        if curr_prefix_sum < min_prefix_sum:
            min_prefix_sum = curr_prefix_sum

        if curr_sum_subarr > max_sum_subarr:
            max_sum_subarr = curr_sum_subarr
    return max_sum_subarr