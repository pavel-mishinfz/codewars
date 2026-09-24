def sort_array(source_array):
    array_odd = [n for n in source_array if n % 2]
    sorted_odd = sorted(array_odd, reverse=True)

    return [n if n % 2 == 0 else sorted_odd.pop() for n in source_array]