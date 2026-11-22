def look_say(n):
    sequence = list(str(n))
    look_say_str = ''
    i = j = 0
    while i < len(sequence):
        cnt = 0
        while j < len(sequence) and sequence[i] == sequence[j]:
            j += 1
            cnt += 1
        look_say_str += f'{cnt}{sequence[i]}'
        i = j
    return int(look_say_str)