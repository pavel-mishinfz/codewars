EMPTY_CELL = ' '
DIRECTIONS = [
    (0, -1),
    (-1, 0),
    (0, 1),
    (1, 0),
]


def find_cells_first_level(mountain, row, col, height):
    cells_first_level = []
    for i in range(row):
        for j in range(col):
            if mountain[i][j] == EMPTY_CELL:
                height[i][j] = -1
                continue
            for d in DIRECTIONS:
                di, dj = d
                ni = i + di
                nj = j + dj
                if (ni < 0 or ni == row) or (nj < 0 or nj == col) or mountain[ni][nj] == EMPTY_CELL:
                    cells_first_level.append((i, j))
                    height[i][j] = 1
    return cells_first_level


def find_next_cells(height, i, j, row, col):
    next_cells = []
    for d in DIRECTIONS:
        di, dj = d
        ni = i + di
        nj = j + dj
        if 0 <= ni < row and 0 <= nj < col and height[ni][nj] == 0:
            next_cells.append((ni, nj))
    return next_cells


def peak_height(mountain):
    row = len(mountain)
    col = len(mountain[0])
    height = [[0] * col for _ in range(row)]

    cells = find_cells_first_level(mountain, row, col, height)
    for curr_cell in cells:
        i, j = curr_cell
        next_cells = find_next_cells(height, i, j, row, col)
        for next_cell in next_cells:
            ni, nj = next_cell
            height[ni][nj] = height[i][j] + 1
            cells.append((ni, nj))

    max_height = -1
    for x in height:
        curr_max = max(x)
        if curr_max > max_height:
            max_height = curr_max
    return 0 if max_height < 0 else max_height
