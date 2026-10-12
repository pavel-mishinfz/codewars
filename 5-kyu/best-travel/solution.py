from itertools import combinations


def choose_best_sum(t, k, ls):
    combs = combinations(ls, k)
    sum_each_comb = [sum(c) for c in combs]
    best_sum = -1
    for x in sum_each_comb:
        if best_sum < x <= t:
            best_sum = x
    return best_sum if best_sum >= 0 else None
