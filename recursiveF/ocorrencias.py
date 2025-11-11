def ocorrencias(lista, x):
    if not lista:
        return 0
    else:
        if lista[0] == x:
            cont = 1
        else:
            cont = 0
        return cont + ocorrencias(lista[1:], x) # enquanto x estiver na sublista, soma 1 ao contador e chama a função novamente com a sublista sem o primeiro elemento
