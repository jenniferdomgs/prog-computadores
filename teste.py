a, b = map(int, input().split())
c = a + b
if a < b:
    c = c * a
else:
    c = c + b
c = c + b // 2
print(c)