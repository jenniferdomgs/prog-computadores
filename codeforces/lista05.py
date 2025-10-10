# A. Corrida

'''N, D, V = map(int, input().split())

N1, D1, V1 = map(int, input().split())

if V / D > V1 / D1:
    print(N)
else:
    print(N1)

# B. Interceptando informações

N1, N2, N3, N4, N5, N6, N7, N8 = map(int, input().split())

lista = [N1, N2, N3, N4, N5, N6, N7, N8]

check = 'S'
for i in lista:
    i = i
    if i != 0 and i!= 1:
        check = 'F'
        break
    if i == lista[-1]:
        check = check
print(check)

# C. Piloto automático

A = int(input())
B = int(input())
C = int(input()) 

v = 0


if (B - A) < (C - B):
    v = 1
elif (B - A) > (C - B):
    v = -1
elif (B - A) == (C - B):
    v = v
print(v)

# D. A idade da Dona Monica

idM = int(input())
idF1 = int(input())
idF2 = int(input())

idF3 = idM - (idF1 + idF2)

maior = 0

lista = [idF1, idF2, idF3]

lista.sort()

print(lista[2])


# E. Conta de água

N = int(input())
valor = 0

if N <= 10:
    valor = 7
elif N <= 30:
    valor = 7 + (N - 10) * 1
elif N <= 100:
    valor = 7 + (20 * 1) + (N - 30) * 2
else:
    valor = 7 + (20 * 1) + (70 * 2) + (N - 100) * 5

print(valor)


# G. Andando no tempo

A, B, C = map(int, input().split())

# se 2 forem iguais ou se a soma de 2 for igual ao terceiro
if (A == B or A == C or B == C or
    A + B == C or A + C == B or B + C == A):
    print("S")
else:
    print("N")

# H. Dupla de Tênis

A = int(input())
B = int(input())
C = int(input())
D = int(input())

lista = [A, B, C, D]
lista.sort()

time1 = int(lista[0]) + int(lista[3])
time2 = int(lista[1]) + int(lista[2])

if time1 > time2:
    print(time1 - time2)
if time2 > time1:
    print(time2 - time1)
if time1 == time2:
    print(0)'''


# I. Máquina de café

A1 = int(input())
A2 = int(input())
A3 = int(input())

# 1º andar
tempo1 = (A2 * 2) + (A3 * 4)

# 2º andar
tempo2 = (A1 * 2) + (A3 * 2)

# 3º andar
tempo3 = (A1 * 4) + (A2 * 2)

print(min(tempo1, tempo2, tempo3))

# J. Capital

A, B, C, D = map(int, input().split())

# o produto de duas tem que ser igual ao produto das outras duas
if (A * B == C * D) or (A * C == B * D) or (A * D == B * C):
    print('S')
else:
    print('N')










