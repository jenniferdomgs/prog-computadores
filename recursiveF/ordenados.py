def ordenada(lista):
    if len(lista) <= 1:
        return True
    return lista[0] <= lista[1] and ordenada(lista[1:])

    
