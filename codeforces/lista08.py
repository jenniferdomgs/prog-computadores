# A. Senha de acesso
'''
senha = int(input())
while senha != 9842:
    print("Senha Invalida!")
    senha = int(input())
print("Acesso Permitido.")

# B. Meia vida
s, m = map(int, input().split())

m = float(m)
seg = 0

while m >= 0.5:
    m /= 2
    seg += s

dias = seg // 86400 # segundos -> dias
segR = seg % 86400 # segundos restantes
h = segR // 3600 # horas
segR %= 3600 # segundos restantes
m = segR // 60 # minutos
segR = segR % 60 # segundos restantes

print(f"{dias} dias {h:02d}:{m:02d}:{segR:02d}")'''


