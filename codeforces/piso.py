L = int(input())
C = int(input())

# lajota tipo 1 preenche tudo
t1 = (L * C) + (L - 1) * (C - 1)

# lajota tipo 2 preenche só as bordas
t2 = (L - 1) * 2 + (C - 1) * 2

print(f"{t1}\n{t2}")


