L, D = map(int, input().split())
K, P = map(int, input().split())

custopercurso = L * K

custopedagio = (L // D) * P

print(custopercurso + custopedagio)