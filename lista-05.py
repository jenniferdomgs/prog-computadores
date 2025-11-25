# A. Tabuada
'''N = int(input())

for i in range(1, 11):
    print(f"{i} x {N} = {i * N}")

# B. Somatório

N = int(input())

# C. Múltiplos I

a, b = map(int, input().split())
list = []

for i in range(1, b + 1):
    if i % a == 0:
        list.append(i)
print(*list)

# D. Divisores

n = int(input())
list = []

for i in range(1, n+1):
    if n % i == 0:
        list.append(i)
print(*list)

# E. Média I

N = int(input())

list = list(map(int, input().split()))

soma = 0
media_check = 0
mediaF = 0

for i in list:
    soma += int(i)
media = soma / N

for i in list:
    if int(i) < media:
        mediaF += 1
    else:
        media_check += 1
print(f"{media:.1f}\n{mediaF}\n{media_check}")

# F. Primo fácil

N = int(input())
div = 0

for i in range(1, N+1):
    if N % i == 0:
        div += 1
if div == 2:
    print("Sim")
else:
    print("Nao")

# G. Média II

n = int(input())
list = list(map(int, input().split()))
soma = 0
list_mediaF = []
list_mediacheck = []

for i in list:
    soma += int(i)
media = soma / n

for i in list:
    if int(i) < media:
        list_mediaF.append(int(i))
    else:
        list_mediacheck.append(int(i))

list_mediaF.insert(0, len(list_mediaF))
list_mediacheck.insert(0, len(list_mediacheck))

print(f"{media:.1f}")
print(*list_mediaF)
print(*list_mediacheck)

# H. Game show

C = int(input())

for i in range(1, C+1):
    V = list(map(int, input().split()))
    
# J. Sequencia secreta

N = int(input())
for i in range(1, N+1):
    V = list(map(int, input().split()))
    
# saída 7 - 3

cont = 0

for i in V:
    if i == V[len-1]:
        cont += 1
print(cont)'''
        
        
# I. Desvendando Monty Hall

N = int(input())

V = list(map(int, input().split()))
    
# a primeira porta escolhida não terá chance

cont = 0
porta = V[0]

for i in V:
    if i != porta:
        cont += 1
    else:
'''
if V[0] == 1:
    for i in V:
        if i == 2 or i == 3:
            cont += 1
elif V[0] == 2:
    for i in V:
        if i == 1 or i == 3:
            cont += 1
        
elif V[0] == 3:
    for i in V:
        if i == 1 or i == 2:
            cont += 1'''
print(cont)
        
