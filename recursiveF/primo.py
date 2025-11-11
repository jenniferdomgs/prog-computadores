from contaDivisores import conta_divisores_main

def primo(n):
    if conta_divisores_main(n) == 2:
        return f"{n} é um número primo"
    else:
        return f"{n} não é um número primo"
    
