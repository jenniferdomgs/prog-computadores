def inverter_lista(lista):
    if len(lista) <= 1:
        return lista
    else:
        return [lista[-1]] + inverter_lista(lista[:-1])
