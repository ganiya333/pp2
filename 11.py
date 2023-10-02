a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
k=int(input())

for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
for i in range(len(a)):
    print(a[i])