import re


def str_to_positive_int_number(s):
    return 1 if s == '' else int(s)


def find_multiplier_right_idx(i, formula):
    j = i + 1
    while j < len(formula) and formula[j].isdigit():
        j += 1
    return j


def parse_molecule(formula):
    pattern = r'([A-Z][a-z]?)([0-9]*)'
    stack = [{}]
    i = 0
    while i < len(formula):
        if formula[i] in '([{':
            stack.append({})
            i += 1
        elif formula[i] in '}])':
            prev_item = stack.pop()
            j = find_multiplier_right_idx(i, formula)
            m = str_to_positive_int_number(formula[i + 1:j])
            new_item = {k: v * m for k, v in prev_item.items()}

            prev_item = stack.pop()
            for k, v in prev_item.items():
                new_item[k] = new_item.get(k, 0) + v
            stack.append(new_item)
            i = j
        else:
            elem, num_str = re.match(pattern, formula[i:]).groups()
            step = len(elem + num_str)
            num = str_to_positive_int_number(num_str)

            prev_item = stack.pop()
            prev_item[elem] = prev_item.get(elem, 0) + num
            stack.append(prev_item)
            i += step
    return stack[-1]