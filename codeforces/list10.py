# A. Chinelos

n = int(input()) # número de tamanhos de chinelo no estoque
lista = [] # lista com todos os dados
cont = 0


for i in range(n):
    x = int(input()) # tamanhos de chinelo
    lista.append(x)

p = int(input()) # quantidade de pedidos

for y in range(p): 
    w = int(input()) # pedidos
      

print(cont)



# imprimir número de pedidos efetivados: todas as aparições do tamanho pedido na lista.
