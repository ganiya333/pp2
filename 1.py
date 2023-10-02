a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])

for i in range(len(a)):
    if i%2==0:
        print(a[i])
    elif i==0:
        print(a[0])