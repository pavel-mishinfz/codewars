def is_prime(x):
    p = 2
    while p*p <= x:
        if x % p == 0:
            return False
        p += 1
    return True

def gap(g, m, n):
    prev_prime = None
    for x in range(m, n+1):
        if is_prime(x):
            if prev_prime and x - prev_prime == g:
                return [prev_prime, x]
            prev_prime = x
    return None
