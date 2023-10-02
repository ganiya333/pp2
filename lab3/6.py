a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])
max=-1e10
idx=0
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        idx=i
print (max,idx)
