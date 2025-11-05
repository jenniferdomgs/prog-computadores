def conta_bits(n):
    if n <= 1:
        return 1
    else:
        return 1 + conta_bits(n // 2)

