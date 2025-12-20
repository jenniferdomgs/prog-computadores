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

print(f"{estadoA}\n{estadoB}")


# D. Enigma

msg = str(input())
crib = str(input())

msgC = len(msg)

cribC = len(crib)

print(msgC // cribC)

# E. Achando monótonos não triviais maximais

n = int(input())
s = input().strip()

total_a = 0   
tamanho_atual = 0  
char_anterior = ''   

for char in s:
    if char == char_anterior:
        # se o caractere é igual ao anterior, att o bloco
        tamanho_atual += 1
    else:
        # se o caractere muda, verifica se o bloco anterior é gual ou maior que 2
        if char_anterior == 'a' and tamanho_atual >= 2:
            total_a += tamanho_atual
        
        # reseta e inicia contagem do novo bloco
        char_anterior = char
        tamanho_atual = 1

if char_anterior == 'a' and tamanho_atual >= 2:
    total_a += tamanho_atual

print(total_a)

# F. Maior número de um algarismo


# G. Flores Florecem da França

while True:
    try:
        linha = input()
        
        if linha == '*':
            break
        
        palavras = linha.split()
        
        letra1 = palavras[0][0].lower() # primeiro caractere do primeiro elemente da lista (letra1 da primeira palavra)
        
        tautogram = True

        for p in palavras:
            if p[0].lower() != letra1:
                tautogram = False
                break 
        
        if tautogram:
            print("Y")
        else:
            print("N")
            
    except EOFError:
        break

# H.Escadinha

N = int(input())
numeros = list(map(int, input().split()))'''

# J.Fase

N = int(input())
C = int(input())
lista = []

for i in range(N):
    inte = int(input())
    lista.append(inte)

lista.sort(reverse=True) # lista em ordem decrescente
clas = C

while clas < N and lista[clas] == lista[C - 1]:
    clas += 1

print(clas)