def enigmatica(n):
    if n == 0:
        return "0"
    if n < 8:
        return str(n)
    else:
        ret = enigmatica(n // 8)
        return ret + str(n % 8)
    

print(enigmatica(65))
print(enigmatica(8))
print(enigmatica(7))
print(enigmatica(0))
print(enigmatica(50))
print(enigmatica(100))
print(enigmatica(255))