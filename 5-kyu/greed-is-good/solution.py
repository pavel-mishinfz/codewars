from collections import Counter


def score(dice):
    cost_combs = {
        0: {},
        1: {
            1: 100,
            5: 50
        },
        2: {
            1: 200,
            5: 100
        },
        3: {
            1: 1000,
            2: 200,
            3: 300,
            4: 400,
            5: 500,
            6: 600
        }
    }

    sum_points = 0
    counter = Counter(dice)
    for num, cnt in counter.items():
        if cnt // 3 > 0:
            sum_points += cost_combs[3].get(num, 0) + cost_combs[cnt % 3].get(num, 0)
        else:
            sum_points += cost_combs[cnt].get(num, 0)
    return sum_points
