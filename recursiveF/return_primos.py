from primo import primo

def return_primos(lista):
    n = len(lista)
    if primo(lista[n-1]) == f"{lista[n-1]} é um número primo":
        if n == 1:
            return [lista[n-1]]
        else:
            return return_primos(lista[:n-1]) + [lista[n-1]]
    else:
        if n == 1:
            return []
        else:
            return return_primos(lista[:n-1])
