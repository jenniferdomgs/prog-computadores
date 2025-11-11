def soma_pares(lista):
    if len(lista) == 0:
        return 0
    elif len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]
        else:
            return 0
    else: 
        if lista[0] % 2 == 0:
            return lista[0] + soma_pares(lista[1:]) # se for par -> valor do elemento + soma do restante da lista 
        else:
            return soma_pares(lista[1:])
