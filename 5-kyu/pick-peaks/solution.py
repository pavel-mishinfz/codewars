def pick_peaks(arr):
    result = {'pos': [], 'peaks': []}
    if len(arr) < 3:
        return result

    i = 1
    while i < len(arr) - 1:
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            result['pos'].append(i)
            result['peaks'].append(arr[i])
        elif arr[i - 1] < arr[i] == arr[i + 1]:
            pos_plateau = i
            while i < len(arr) - 1:
                if arr[i] < arr[i + 1]:
                    break
                if arr[i] > arr[i + 1]:
                    result['pos'].append(pos_plateau)
                    result['peaks'].append(arr[pos_plateau])
                    break
                i += 1
        i += 1
    return result

# use more elegant solution
# def pick_peaks(arr):
#     result = {'pos': [], 'peaks': []}
#     if len(arr) < 3:
#         return result
#
#     potential_pos = i = 1
#     potential_peak = False
#     while i < len(arr):
#         if arr[i - 1] < arr[i]:
#             potential_peak = True
#             potential_pos = i
#         elif arr[i - 1] > arr[i] and potential_peak:
#             result['pos'].append(potential_pos)
#             result['peaks'].append(arr[potential_pos])
#             potential_peak = False
#         i += 1
#     return result