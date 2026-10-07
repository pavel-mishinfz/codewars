def is_solved(board):
    win_combs = [
        board[0],
        board[1],
        board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]

    if any([1, 1, 1] == comb for comb in win_combs):
        return 1
    elif any([2, 2, 2] == comb for comb in win_combs):
        return 2
    elif any(0 in comb for comb in win_combs):
        return -1
    else:
        return 0