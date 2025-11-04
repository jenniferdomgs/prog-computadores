def conta_divisores(n):
    if n % 2 == 0: # caso base -> pois, se for par, n/2 é o número de divisores
        return n // 2
    else: 
        conta_divisores = 0
        for i in range(1, n + 1): # para cada i de 1 a n, verifica se i divide n (resto=0 : i é divisor)
            if n % i == 0:
                conta_divisores += 1 # add 1 a cada caso verdadeiro
        return conta_divisores
    