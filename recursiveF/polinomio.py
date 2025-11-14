def polinomio(coeficientes, x):
    if len(coeficientes) == 1: # quando a lista tem apenas 1 elemento, o pol é o próprio coeficiente
        return coeficientes[0]
    else: 
        # Pn(x) = x.Pn−1(x) + an -> an: ultimo coeficiente da lista atual
        return x * polinomio(coeficientes[:-1], x) + coeficientes[-1]
    