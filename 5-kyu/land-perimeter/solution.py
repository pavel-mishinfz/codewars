ISLAND = 'X'
WATER = 'O'
DIRECTIONS = [
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0),
]


def land_perimeter(arr):
    perimeter = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == ISLAND:
                for di, dj in DIRECTIONS:
                    ni = i + di
                    nj = j + dj
                    if ni < 0 or ni == len(arr) or nj < 0 or nj == len(arr[0]) or arr[ni][nj] == WATER:
                        perimeter += 1
    return f'Total land perimeter: {perimeter}'