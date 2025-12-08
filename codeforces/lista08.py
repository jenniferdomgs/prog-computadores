# A. Senha de acesso

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

print(f"{dias} dias {h:02d}:{m:02d}:{segR:02d}")

# C. Pula sapo

p, n = map(int, input().split())
h = list(map(int, input().split()))
status = "YOU WIN"

for i in range(n - 1):
    cano_atual = h[i]
    prox_cano = h[i+1]
    
    # calculo da diferença absoluta 
    diferenca = abs(prox_cano - cano_atual)
    
    if diferenca > p:
        status = "GAME OVER"
        break 

print(status)

# D. Número primo
def primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
prox_primo = n + 1

while True:
    if primo(prox_primo):
        print(prox_primo)
        break
    prox_primo += 1

# E. Blobs

n = int(input())

for i in range(n):
    c = float(input())
    dias = 0
    while c > 1.0:
        c /= 2
        dias += 1
    print(f"{dias} dias")


# F. Alarme despertador

while True:
    try:
        H1, M1, H2, M2 = map(int, input().split())

        # para quando as variaveis são 0
        if H1 == 0 and M1 == 0 and H2 == 0 and M2 == 0:
            break

        min_iniciais = H1 * 60 + M1
        min_alarme = H2 * 60 + M2

        min_dormidos = 0
        if min_alarme > min_iniciais:
            # 1 -> alarme mesmo dia
            min_dormidos = min_alarme - min_iniciais
        else:
            # 2 -> dia seguinte
            min_dormidos = (1440 - min_iniciais) + min_alarme
        
        print(min_dormidos)

    except (EOFError, ValueError):
        break


# G. O troco

t = int(input()) # testes

for i in range(t):
    d, n = map(int, input().split()) # dinheiro / marcas
    preco = list(map(float, input().split()))
    t_max = 0.0

    cont = 0
    while cont < n:
        preco_atual = preco[cont]
        if preco_atual < d:
            t_atual = d % preco_atual
            if t_atual > t_max:
                t_max = t_atual
        cont += 1 
    print(f"{t_max:.2f}")

# H. Loop musical

while True:
    try:
        n = int(input())
        # parada
        if n == 0:
            break

        h = list(map(int, input().split()))
        
        h_extended = [h[-1]] + h + [h[0]] # lista estendida p/ verificação 
        
        picos = 0

        for i in range(1, n + 1):
            anterior = h_extended[i - 1]
            atual = h_extended[i]
            proximo = h_extended[i + 1]
            
            if (atual > anterior and atual > proximo) or (atual < anterior and atual < proximo):
                picos += 1
                
        print(picos)

    except (EOFError, ValueError):
        break

# I. Descobrindo senha

cont = 1  # contador de testes

while True:
    try:
        n = int(input())
    except EOFError:
        break

    v = list(map(float, input().split()))
    valores = []

    for i in v:
        valores.append(float(i))

    lista = [] 

    # pares de oleo + digito
    for l in range(10):
        lista.append([valores[l], l])

    # ordenando os valores dos oleos de forma decrescente
    # se tiver empate, compara os digitos e ordena de forma crescente
    tam = len(lista)
    for i in range(tam):
        for j in range(tam - 1 - i):
            oleo1, dig1 = lista[j]
            oleo2, dig2 = lista[j+1]

            troca = False
            if oleo2 > oleo1:
                troca = True
            elif oleo2 == oleo1 and dig2 < dig1:
                troca = True

            if troca:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    # ordenando os n primeiros
    senha = ""
    for i in range(n):
        senha += str(lista[i][1])

    print(f"Caso {cont}: {senha}")
    cont += 1

# J. Mergulho

N, R = map(int, input().split())
id = list(map(int, input().split()))

out = []

if N == R:
    print("*")
else:
    for i in range(1, N+1):
        if i in id:
            continue
        else:
            out.append(i)
    print(*out)







