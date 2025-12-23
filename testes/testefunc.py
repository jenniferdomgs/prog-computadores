# codigos prova 3 - prog. de computadores

def func(l01):
    k = 0
    for i in range(1, len(l01)):
        if l01[i] > l01[i - 1]:
            k = k + l01[i]
    return k

lista = list(map(int, input().split()))
lista.append(13)
q = func(lista)
print(q)

def func1(l01):
    k = 0
    for i in range (1 , len ( l01 )):
        if l01 [i] < l01 [i - 1]:
            k = k + 1
    return k

lista = list(map(int, input().split()))
lista.append(1)
q = func1(lista)
print(q)

def func2(l01, num):
    q = 0
    for i in range ( len ( l01 )):
        for j in range (i + 1, len ( l01 )):
            if ( l01 [i] + l01 [j ]) >= num :
                q = q + 1
    return q

n = int (input())
lista = list(map(int, input().split()))
lista.append(n - 1)
print(func2(lista, n))


# verifica 2 listas e retorna os valores da 2 que não estão na 1

lista01 = list(map(int, input().split()))
lista02 = list(map(int, input().split()))

resultado = [x for x in lista02 if x not in lista01]
print(*resultado)

def dif_listas(l1, l2):
    resultado = [x for x in l2 if x not in l1]
    return resultado

