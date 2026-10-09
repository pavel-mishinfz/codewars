def dir_reduc(arr):
    opp = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

    new_arr = []
    for x in arr:
        if new_arr and new_arr[-1] == opp[x]:
            new_arr.pop()
        else:
            new_arr.append(x)
    return new_arr

# use recursion
# def dir_reduc(arr):
#     arr_as_str = ' '.join(arr)
#     arr_as_str = arr_as_str.replace('NORTH SOUTH', '').replace('SOUTH NORTH', '').replace('WEST EAST', '').replace('EAST WEST', '')
#     new_arr = arr_as_str.split()
#     return dir_reduc(new_arr) if len(new_arr) < len(arr) else new_arr