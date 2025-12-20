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