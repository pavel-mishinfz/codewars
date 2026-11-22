def create_spiral(n):
    if not isinstance(n, int) or n < 1:
        return []

    j = 0
    value = 1
    N = [[0] * n for _ in range(n)]
    while value <= n ** 2:
        for side in ['TOP', 'RIGHT', 'BOTTOM', 'LEFT']:
            for i in range(j, n - j):
                match side:
                    case 'TOP':
                        if N[j][i] == 0:
                            N[j][i] = value
                            value += 1
                    case 'RIGHT':
                        if N[i][n - j - 1] == 0:
                            N[i][n - j - 1] = value
                            value += 1
                    case 'BOTTOM':
                        if N[n - j - 1][n - i - 1] == 0:
                            N[n - j - 1][n - i - 1] = value
                            value += 1
                    case 'LEFT':
                        if N[n - i - 1][j] == 0:
                            N[n - i - 1][j] = value
                            value += 1
        j += 1
    return N