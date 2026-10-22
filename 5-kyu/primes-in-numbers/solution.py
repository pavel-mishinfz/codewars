def prime_factors(n):
    prime_factors = []
    x = 2
    while x * x <= n:
        cnt = 0
        while n % x == 0:
            n //= x
            cnt += 1

        if cnt > 0:
            prime_factors.append((x, cnt))

        x += 1

    prime_factors.append((n, 1))
    prime_factors.sort(key=lambda x: x[0])
    result = ''
    for x in prime_factors:
        a, b = x
        if b > 0:
            result += f'({a})' if b == 1 else f'({a}**{b})'
    return result
