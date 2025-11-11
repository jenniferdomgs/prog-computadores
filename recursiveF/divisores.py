def divisores_main(n, k):
    # no caso base temos que se k for maior, não tem mais divisores
    if k > n:
        return []
    # encontra o próximo divisor
    div = divisores_main(n, k + 1)
    # se k é divisor = conta 1 divisor
    if n % k == 0:
        return [k] + div # add k na lista de divisores já encontrados
    else:
        return div # retorna os divs ja encontrados sem k

def divisores(n):
    return divisores_main(n, 1)
