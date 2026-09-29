def solution(s):
    left, right = 0, 0

    break_up_camel_casing = []
    for ch in s:
        if ord('A') <= ord(ch) <= ord('Z'):
            word = s[left:right]
            break_up_camel_casing.append(word)
            left = right
        right += 1
    last_word = s[left:right]
    break_up_camel_casing.append(last_word)
    return ' '.join(break_up_camel_casing)
    # or use isupper()
    # return ''.join([' ' + ch if ch.isupper() else ch for ch in s])