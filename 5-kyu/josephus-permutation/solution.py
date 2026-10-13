def josephus(items,k):
    josephus_permutation = []
    new_idx = 0
    while items:
        new_idx = (new_idx + k - 1) % len(items)
        x = items[new_idx]
        josephus_permutation.append(x)
        items.pop(new_idx)
    return josephus_permutation