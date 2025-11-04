from list_01 import conta_divisores

def primo(n):
    if conta_divisores(n) == 2:
        return f"{n} é um número primo"
    else:
        return f"{n} não é um número primo"
    