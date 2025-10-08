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

print(lista[2])'''

F, B, M = map(int, input().split())
Rf, Rb, Rm = map(int, input().split())


