a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
cnt=1
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        cnt+=1
print (cnt)