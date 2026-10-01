def solution(number):
    if number < 0:
        return 0

    multiple_three = [i for i in range(3, number, 3)]
    multiple_five = [j for j in range(5, number, 5)]

    return sum(set(multiple_three + multiple_five))
