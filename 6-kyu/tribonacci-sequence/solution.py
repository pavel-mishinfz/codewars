def tribonacci(signature, n):
    n_tribonacci = []

    for i in range(n):
        if i < 3:
            n_tribonacci.append(signature[i])
        else:
            n_tribonacci.append(sum(n_tribonacci[i-3:i]))
    return n_tribonacci