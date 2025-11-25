def ackermann(m, n):
    ackermann.chamadas += 1
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 0)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

ackermann.chamadas = 0
m, n = 1, 4
resultado = ackermann(m, n)

print(f"({m}, {n})")
print(f"  -> Resultado: {resultado}")
print(f"  -> Número de chamadas: {ackermann.chamadas}")
