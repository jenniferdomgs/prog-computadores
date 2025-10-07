# A. Frota de Taxi

A, G, Ra, Rg = map(float, input().split())

custoA = A / Ra
custoG = G / Rg

if custoA < custoG:
    print("A")
else:
    print("G")

# B. Triângulo

A, B, C, D = map(int, input().split())

if ((A + B > C and A + C > B and B + C > A) or  
    (A + B > D and A + D > B and B + D > A) or 
    (A + C > D and A + D > C and C + D > A) or  
    (B + C > D and B + D > C and C + D > B)):   
    print("S")
else:
    print("N")

# C. Maior de 5 números

u = int(input())
d = int(input())
t = int(input())
q = int(input())
c = int(input())

maior = u

if d >= maior:
    maior = d
if t >= maior:
    maior = t
if q >= maior:
    maior = q
if c >= maior:
    maior = c

print(maior)

# D. Tanque de combustível

C = int(input())
D = int(input())
T = int(input())

combN = D / C

combComprar = combN - T

if combComprar < 0:
    combComprar = 0.0

print(f"{combComprar:.1f}")

L = int(input())
C = int(input())
branca = 1
preta = 0
if (L + C) % 2 == 0:
    # par é branca
    print(branca)
else:
    # impar é preta
    print(preta)

# F. Maior média ponderada

a11, a21 = map(int, input().split())
a12, a22 = map(int, input().split())
p1, p2 = map(int, input().split())

m1 = ((a11 * p1) + (a21 * p2)) // (p1 + p2)
m2 = ((a12 * p1) + (a22 * p2)) // (p1 + p2)

if m1 >= m2:
    print(1)
else:
    print(2)

# G. Idade de Camila

# Cibele > Camila > Celeste
I = int(input())
Ii = int(input())
Iii = int(input())

if (Ii >= I and I >= Iii) or (Iii >= I and I >= Ii):
    print(I)
elif (I >= Ii and Ii >= Iii) or (Iii >= Ii and Ii >= I):
    print(Ii)
else:
    print(Iii)

# forma mais direta

idades = [int(input()), int(input()), int(input())]
idades.sort()

print(idades[1])

# H. Teleférico

C = int(input())
A = int(input())

CapA = C - 1

viagens = A // CapA

if A % CapA != 0:
    viagens += 1

print(viagens)

# I. Triângulos

A, B, C = map(int, input().split())

if A >= B and A >= C:
    maior, l1, l2 = A, B, C
elif B >= A and B >= C:
    maior, l1, l2 = B, A, C
else:
    maior, l1, l2 = C, A, B

if l1 + l2 <= maior:
    print("n")
else:
    if maior**2 > l1**2 + l2**2:
        print("o") 
    elif maior**2 == l1**2 + l2**2:
        print("r") 
    else:  
        print("a") 

# J. Nota Cortada

B = int(input())
T = int(input()) 

if (B + T) > 160:
    print(1) # felix ganha
elif (B + T) < 160:
    print(2) # marzia ganha
else: # (B + T) == 160
    print(0) # ninguém 





