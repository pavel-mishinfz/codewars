def find_uniq(arr):
    sorted_arr = sorted(arr)
    return sorted_arr[-1] if sorted_arr[0] == sorted_arr[1] else sorted_arr[0]