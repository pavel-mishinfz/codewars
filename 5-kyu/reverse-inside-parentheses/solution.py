def reverse_in_parentheses(s):
    stack = []
    for i in range(len(s)):
        ch = s[i]
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            j = stack.pop()
            tmp = s[j+1:i]
            s = s[:j+1] + tmp[::-1].translate(str.maketrans('()', ')(')) + s[i:]
    return s