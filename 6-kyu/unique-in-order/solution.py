# you can use groupby from itertools
def unique_in_order(sequence):
    unique_items = []

    prev_item = None
    for curr_item in sequence:
        if prev_item != curr_item:
            unique_items.append(curr_item)
        prev_item = curr_item
    return unique_items