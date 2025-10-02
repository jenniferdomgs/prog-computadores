nome = input()
salario = float(input())
vendas = float(input())

com = (vendas * 15) / 100

print(f"{nome}\nR$ {salario + com:.2f}")