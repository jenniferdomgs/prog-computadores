d = int(input())
v = int(input())

h1 = d / v 

h2 = int(h1)

m = (h1 - h2) * 60

m = int(m)

print(f"{h2:02}:{m:02}")
