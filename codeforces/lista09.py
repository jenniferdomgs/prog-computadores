# A. Jogo da estratégia
'''J, R = map(int, input().split())
v = list(map(int, input().split()))

pontos = [0] * J # cada indice corresponde ao jogador i+1 
# 0 (Jogada 1) -> Jogador 1 // j-1 (ultima rodada) -> Jogador J // j (primeira: proxima rodada) -> Jogador 1

for i in range(len(v)):
    index_jogador = i % J
    
    # add pontos ao jogador da vez
    pontos[index_jogador] += v[i]

vencedor = 0
max_pontos = 0

for i in range(J): # pega o maior ou o último (empate)
    pontos_atual = pontos[i]
    jogador_atual = i + 1

    if pontos_atual > max_pontos:
        max_pontos = pontos_atual
        vencedor = jogador_atual
    elif pontos_atual == max_pontos:
        vencedor = jogador_atual

print(vencedor)
        

# B. Holter

N = int(input())
valores = []
for i in range(N):
    b = int(input())
    valores.append(b)

media = 0

for i in valores:
    media += i

media = media // N

media_out = []

for i in valores:
    if i < int(media * 0.9) or i > int(media * 1.1): # se o valor medido estiver fora da faixa de 10%, add ele a uma lista  
        media_out.append(i)

tam = len(media_out)
print(f"{media}\n{tam}")

# C. Lâmpadas

N = int(input()) 
inter = list(map(int, input().split()))

estadoA = 0
estadoB = 0

for i in inter:
    if i == 1:
        if estadoA == 0:
            estadoA = 1
        else:
            estadoA = 0
    if i == 2:
        if estadoA == 1 and estadoB == 0:
            estadoA = 0
            estadoB = 1
        elif estadoA == 0 and estadoB == 1:
            estadoA = 1   
            estadoB = 0  
        elif estadoA == 1 and estadoB == 1:
            estadoA = 0
            estadoB = 0
        else:
            estadoA = 1
            estadoB = 1 

print(f"{estadoA}\n{estadoB}")'''


# D. Enigma

msg = str(input())
crib = str(input())

# D. Enigma

msg = str(input())
crib = str(input())

msgC = len(msg)
 
cribC = len(crib)

cont = 0

for i in range(msgC - cribC):
    if (msgC - cribC) % 2 == 0:
        cont = msgC // cribC
    if (msgC - cribC) % 2 != 0:
        cont += 1

print(cont)


