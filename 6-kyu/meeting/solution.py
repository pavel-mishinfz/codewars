def meeting(s):
    s_as_list = [person.split(':') for person in s.upper().split(';')]
    s_sorted = sorted(s_as_list, key=lambda x: (x[1], x[0]))
    return ''.join(f'({last_name}, {first_name})' for first_name, last_name in s_sorted)
