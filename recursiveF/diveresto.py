def misteriosa(a, b):
    if a < b:
        return [0, a]
    else:
        x = misteriosa(a - b, b)
        x[0] += 1
        return x
    
print(misteriosa(20, 3))
print(misteriosa(20, 4))
print(misteriosa(30, 4))
print(misteriosa(30, 8))
print(misteriosa(41, 3))
print(misteriosa(42, 3))