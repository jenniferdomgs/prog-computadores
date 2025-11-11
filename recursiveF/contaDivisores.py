def conta_divisores(n, d):
    if d == 1:
        return 1
    if n % d == 0:
        return 1 + conta_divisores(n, d -1)
    else:
        return 0 + conta_divisores(n, d -1)

def conta_divisores_main(n):
    return conta_divisores(n, n)

