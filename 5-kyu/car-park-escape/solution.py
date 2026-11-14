def escape(carpark):
    start_idx = -1
    i = 0
    while start_idx == -1:
        lvl = carpark[i]
        start_idx = lvl.index(2) if 2 in lvl else -1
        i += 1

    j = i - 1
    result = []
    while j < len(carpark):
        lvl = carpark[j]
        next_idx = lvl.index(1) if 1 in lvl else len(lvl) - 1
        is_first_stage = False if 1 in lvl else True
        cnt = start_idx - next_idx
        if cnt > 0:
            result.append(f'L{cnt}')
        elif cnt < 0:
            result.append(f'R{abs(cnt)}')
        if is_first_stage:
            return result
        result.append(f'D1')
        if 'D' in result[-2]:
            prev_step = result.pop()
            result[-1] = f'D{int(result[-1][1]) + int(prev_step[1])}'
        start_idx = next_idx
        j += 1
    return result