N, M = map(int, input().split())
anya = set()
borya = set()
for _ in range(N):
    color = int(input())
    anya.add(color)
for _ in range(M):
    color = int(input())
    borya.add(color)
cc = anya.intersection(borya)
ua = anya.difference(borya)
ub = borya.difference(anya)
print(len(cc))
print(*sorted(cc))

print(len(ua))
print(*sorted(ua))

print(len(ub))
print(*sorted(ub))