def func(l, n):
    q = 0
    for i in range(1, len(l)):
        for j in range(0, i):
            if l[i] + l[j] == n:
                q = q + 1
    return q

n = int(input())
l = list(map(int, input().split()))
print(func(l, n))