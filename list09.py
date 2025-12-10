# A. Jogo da estratégia
J, R = map(int, input().split())
v = list(map(int, input().split()))

contR = 0
contJ = 0
maior = 0
for i in v:
    if i >= v[i+1]:
        maior = i
        if R == J:
            contJ += 1
            contR += 1
            if contR == R:
                print(contJ)
                
        else:
            print("teste")
        

# B. Holter
'''
N = int(input())
valores = []
for i in range(N):
    b = list(map(int, input().split()))

for i in b:

    valores.append(int(i))
'''

