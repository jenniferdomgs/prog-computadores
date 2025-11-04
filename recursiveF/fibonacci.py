def fibonacci(n): # cada termo é a soma dos 2 anteriores
    # casos base
    if n == 1: # se n é 1 (=0, pois a contagem começa do 0)
        return 0
    elif n == 2: # se n é 2 (=1, pois 0+1=1)
        return 1 
    
    else: # casos recursivos (ou seja, fora dos casos base -> chama-se a função dentro da própria)
        return fibonacci(n - 1) + fibonacci(n - 2)

