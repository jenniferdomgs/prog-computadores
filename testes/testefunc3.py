def f4(l1, l2):
    ans = 0
    for i in range(len(l1)):
        for j in range(i + 1, len(l2)):
            if l1[i] == l2[j]:
                ans += 1
                break
    return ans

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(f4(l1, l2))