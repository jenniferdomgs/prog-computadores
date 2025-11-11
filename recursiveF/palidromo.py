def palindromo(s):
    if s[::-1] == s:
        return f"{s} é um palíndromo"
    else:
        return f"{s} não é um palíndromo"

def palindromoR(s):
    if len(s) <= 1:
        return "é um palíndromo"
    if s[0] != s[-1]:
        return "não é um palíndromo"
    return palindromoR(s[1:-1]) # se a primeira e a ulima letra são iguais, chama a função novamente sem elas

