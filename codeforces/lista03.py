#A: Iguais
a = int(input())
b =int(input())

if a == b:
    print("Sim")
else:
    print("Nao")

    

#B: Maior de 2
a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)



# C: Maior de 3
a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(a)
else:
    if b >= a and b >= c:
        print(b)
    else:
        if c >= a and c >= b:
            print(c)


# D: Par ou Ímpar
num = int(input())

if num % 2 == 0:
    print("Par")
else:
    print("Impar")



# E: Sucessor par
num = int(input())

if num % 2 == 0:
    print(num + 2)
else:
    print(num + 1)


# F: Lanche
cod, cont = map(int, input().split())

if cod == 1:
    print(f"Total: R$ {cont * 4.00:.2f}")
elif cod == 2:
    print(f"Total: R$ {cont * 4.50:.2f}")
elif cod == 3:
    print(f"Total: R$ {cont * 5.00:.2f}")
elif cod == 4:
    print(f"Total: R$ {cont * 2.00:.2f}")
elif cod == 5:
    print(f"Total: R$ {cont * 1.50:.2f}")


# G: Múltiplos 
a = int(input())
b = int(input())

if a % b == 0:
    print("Multiplos")
elif b % a == 0:
    print("Multiplos")
else:
    print("Nao multiplos")


# H: Coordenadas de um ponto
x, y = map(float, input().split())


if x == 0 and y == 0:
    print("Origem")
elif x == 0 and y != 0:
    print("Eixo Y")
else:
    if x != 0 and y == 0:
        print("Eixo X")
    elif x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    else:
        print("Q4")


# I: Sedex
D = int(input())
A, L, P = map(int, input().split())

if (D <= A) and (D <= L) and (D <= P):
    print("S")
else:
    print("N")


# J: Tira-teima
x, y = map(int, input().split())

if x >= 0 and x <= 432 and y >= 0 and y <= 468:
    print("dentro")
else:
    print("fora")











