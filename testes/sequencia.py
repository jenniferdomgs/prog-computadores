def sequencia(lista):
    if not lista:
        return 0, 0, 0
    
    melhor_tam = 0
    melhor_num = lista[0]
    melhor_ind = 0
    
    atual_tam = 1
    atual_num = lista[0]
    atual_ind = 0
    
    for i in range(1, len(lista)):
        if lista[i] == lista[i-1]:
            # se é igual ao anterior att a sequencia atual
            atual_tam += 1
        else:
            # se mudou o número, verifica se a sequencia atual é a maior
            if atual_tam > melhor_tam:
                melhor_tam = atual_tam
                melhor_num = atual_num
                melhor_ind = atual_ind
            
            # reseta a seq atual
            atual_tam = 1
            atual_num = lista[i]
            atual_ind = i
            
    # checa no final para verificar se a melhor seq é a última
    if atual_tam > melhor_tam:
        melhor_tam = atual_tam
        melhor_num = atual_num
        melhor_ind = atual_ind
        
    return melhor_tam, melhor_num, melhor_ind

lista = list(map(int, input().split()))
print(sequencia(lista))

