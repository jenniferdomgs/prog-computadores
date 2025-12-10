# A. Jogo da estratégia
J, R = map(int, input().split())
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
'''
N = int(input())
valores = []
for i in range(N):
    b = list(map(int, input().split()))

for i in b:

    valores.append(int(i))
'''

