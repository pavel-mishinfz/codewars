def valid_braces(string):
    stack = []
    for br in string:
        len_stack = len(stack)
        if br == ')' and len_stack > 0 and stack[-1] == '(':
            stack.pop()
        elif br == '}' and len_stack > 0 and stack[-1] == '{':
            stack.pop()
        elif br == ']' and len_stack > 0 and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(br)
    return len(stack) == 0