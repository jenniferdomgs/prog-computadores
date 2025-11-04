def conta_divisores(n):
    # casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n != 2 or n % 2 == 0: # pois, se for par, n/2 é o número de divisores (exceto no caso do 2)
        return n // 2
    else: 
        cont = 2 # no caso do 2 e dos impares tem COM CERTEZA 2 divisores (ele mesmo e 1)
        if conta_divisores(n+1) == cont:
            return cont
        else:
            return conta_divisores(n+1) - 1
        
print(conta_divisores(3))
