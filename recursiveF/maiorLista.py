def indice_do_maior(lista):
    if len(lista) == 1:
        return 0
    index_maior = indice_do_maior(lista[1:]) # cria uma nova lista sem o primeiro elemento
    if lista[0] >= lista[index_maior + 1]: # comparando o maior da lista original com o maior da sublista
        return 0
    else:
        return index_maior + 1

    
