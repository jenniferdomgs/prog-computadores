# E. Dia da semana

def dia_da_semana(h, d):
    dias = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    h = h.capitalize()
    for i in dias:
        if i == h:
            return dias[(dias.index(i) + d) % 7]
        
# G. Dia por extenso

def dia(dia, mes, ano):
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    if not (1 <= mes <= 12 and 1 <= dia <= 31):
        return 'Data Invalida'
    
    diasMes = 31

    if mes == 2:
        diasMes = 28
    elif mes in [4, 6, 9, 11]:
        diasMes = 30
    if dia > diasMes:
        return 'Data Invalida'
    
    return f'{dia:02d} de {meses[mes - 1]} de {ano}'

# H. Média

def media_lista(lista):
    x = 0
    for i in lista:
        x += i  
    return x // len(lista)

# I. Troca de menor com primeiro

def lista_troca_menor_primeiro(lista):
    if len(lista) < 2:
        return 0

    indice_menor = lista.index(min(lista))
    if indice_menor != 0:
        lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
        return 1
    else:
        return 0

# J. Lista sem menor

def sublista_sem_menor(lista):
    if not lista:
        return []
    nova_lista = lista.copy()
    menor = min(nova_lista)
    nova_lista.remove(menor)
    return nova_lista




