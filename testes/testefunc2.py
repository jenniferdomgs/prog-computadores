def g(l):
    if len(l) == 0:
        return 10
    else:
        n = l[-1]
        if n % 2 == 1:
            return 1 + g(l[:-1])
        else:
            return 10 * g(l[:-1])
        
lista = list(map(int, input().split()))
lista.append(len(lista))
lista.append(2)
print(g(lista))