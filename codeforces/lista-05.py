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
    print("Nao")'''

# G. Média II

n = int(input())
list = list(map(int, input().split()))
soma = 0
list_mediaF = []
list_mediacheck = []

for i in list:
    soma += int(i)
media = soma // n

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


