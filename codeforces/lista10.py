# A. Chinelos
'''
n = int(input()) # número de tamanhos de chinelo no estoque
lista = [] # lista com todos os dados
cont = 0

for i in range(n):
    x = int(input()) # tamanhos de chinelo
    lista.append(x)

p = int(input()) # quantidade de pedidos

for y in range(p): 
    w = int(input()) # tamanho do pedido atual
    
    if lista[w - 1] > 0:
        cont += 1          # conta a venda
        lista[w - 1] -= 1  # subtrai o chinelo

print(cont)

# B. OBI

n, p = map(int, input().split()) # n: competidores p: minimo de pontos p/ ser convidado
cont = 0

for i in range(n):
    f1, f2 = map(int, input().split())
    if f1 + f2 >= p:
        cont += 1
print(cont)

# C. Repetições

dna = str(input())
dna = dna.upper()
maior = 1
atual = 1

for i in range(1, len(dna)):
    if dna[i] == dna[i - 1]:
        atual += 1
    else:
        if atual > maior:
            maior = atual
        atual = 1

if atual > maior:
    maior = atual  

print(maior)


# D. Calçada imperial

N = int(input())
seq = []

# maior sequencis que alterna entre 2 números

for i in range(N):
    seq.append(int(input()))

resposta = 1

# escolhe o primeiro
for i in range(N):
    # escolhe o segundo
    for j in range(i+1, N):
        if seq[j] == seq[i]: # se forem iguais -> pula até achar 2 distintos
            continue
        atual = seq[i]
        prox = seq[j]
        resposta_atual = 2

        for k in range(j+1, N): # percorre o resto da seq para contar quantas vezes consegue continuar
            if seq[k] == atual:
                resposta_atual = resposta_atual + 1
                # se acha o primeiro, começa a procurar o segundo e vice-versa
                atual, prox = prox, atual
        if resposta_atual > resposta:
            resposta = resposta_atual

print(resposta)

# E. Saltadores alegres

while True:
    try:
        linha = input()
        
        # transformando em int
        valores = list(map(int, linha.split()))
        
        # se for linha em branco -> pula
        if not valores:
            continue

        # primeiro numero = tamanho N
        n = valores[0]
        
        # o resto é a seq
        sequencia = valores[1:]

        # 1 = alegre
        if n == 1:
            print("Alegre")
            continue

        # diferenças sem repetição
        diferencas = set()
        
        # válidação das diferenças
        for i in range(n - 1):
            valor_atual = sequencia[i]
            proximo_valor = sequencia[i+1]
            
            # diferença absoluta
            diff = abs(valor_atual - proximo_valor)
            
            # a diferença tem que ser maior que 0 e menor que N
            if 0 < diff < n:
                diferencas.add(diff)
        
        # se tiver (n-1) diferenças únicas no conjunto -> já foram todos os números de 1 até n-1
        if len(diferencas) == n - 1:
            print("Alegre")
        else:
            print("Nao alegre")

    except EOFError:
        break

# F. Fita colorida

N = int(input())
fita = list(map(int, input().split()))
cores = [100] * N # valor inicial
dist = 100

# percorrendo da esquerda p/ direita
for i in range(N):
    if fita[i] == 0:
        dist = 0
    else:
        dist += 1
    cores[i] = min(cores[i], dist)

# percorrendo da direita p/ esquerda
for i in range(N -1, -1, -1):
    if fita[i] == 0:
        dist = 0
    else:
        dist += 1
    cores[i] = min(cores[i], dist)

# limitando a 9
for i in range(N):
    if cores[i] >= 9:
        cores[i] = 9

print(*cores)
    

# G. Batalha naval

N = int(input())
tab = [[0] * 11 for _ in range(11)] # tabueiro 11x11
valido = True

for i in range(N):
    D, L, R, C = map(int, input().split())
    
    if not valido:
        continue

    if D == 0: # horizontal
        if C + L - 1 > 10: # verifica se sai do tabuleiro
            valido = False
        else:
            for k in range(L):
                if tab[R][C + k] == 1: # verifica sobreposição
                    valido = False
                    break
                tab[R][C + k] = 1
    else: # vertical
        if R + L - 1 > 10: # verifica se sai do tabuleiro
            valido = False
        else:
            for k in range(L):
                if tab[R + k][C] == 1: # verifica sobreposição
                    valido = False
                    break
                tab[R + k][C] = 1

if valido:
    print("Y")
else:
    print("N")

# H. Subsequencia

A, B = map(int, input().split())

seqA = list(map(int, input().split()))
seqB = list(map(int, input().split()))
indexB = 0

for i in seqA:
    if i == seqB[indexB] and B > indexB:
        indexB += 1
    if indexB == B:
        break

if indexB == B:
    print("S")
else:
    print("N")

# I. Progressões aritméticas

N = int(input())
lista = list(map(int, input().split()))

if N <= 2: # se tiver até 2 elementos já é uma PA
    print(1)
else:
    partes = 1
    tam_atual = 2

    while tam_atual < N:
        # diferença atual e anterior
        dif_atual = lista[tam_atual] - lista[tam_atual - 1]
        # diferença anterior e anterior dele
        dif_anterior = lista[tam_atual - 1] - lista[tam_atual - 2]
        if dif_atual == dif_anterior: # continua
            tam_atual += 1
        else:
             # quebra
            partes += 1
            tam_atual += 1 # pula o prócimo -> nova seq
            tam_atual += 1
    print(partes)'''

# J. Escada perfeita

N = int(input())
lista = list(map(int, input().split()))

pedras = sum(lista) # total de pedras

soma_base = (N * (N - 1)) // 2

resto = pedras - soma_base

# se o resto for menor que 0 ou se o resto não for divisível por N 
if resto < 0 or resto % N != 0:
    print("-1")
else:
    # altura do primeiro degrau
    altura_inicial = resto // N
    
    cont = 0 # contador de movimentos necessários
    
    # contagem dos blocos que ficam sobrando
    for i in range(N):
        altura_necessaria = altura_inicial + i
        
        # se a pilha atual é maior -> tem excesso
        if lista[i] > altura_necessaria:
            cont += (lista[i] - altura_necessaria)
            
    print(cont)