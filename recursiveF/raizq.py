def raiz_quadradaR(n, tentativa, erro):
    if abs(tentativa ** 2 - n) <= erro: # abs é o valor absoluto // a aproximação é boa se o quadrado do chute ta proximo de n e dentro da margem de erro
        return tentativa
    else: # calcula um chute melhor
        nova_tentativa = (tentativa + n / tentativa) / 2
        return raiz_quadradaR(n, nova_tentativa, erro)

def raiz_quadrada(n, erro=0.0001):
    if n < 0:
        return "Não é possível calcular a raiz quadrada de um número negativo."
    if n == 0:
        return 0.000
    resultado = raiz_quadradaR(n, n / 2.0, erro)
    return f"{resultado:.3f}"




