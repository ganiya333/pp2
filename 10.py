a=input().split()
for i in range (len(a)):
    a[i]=int(a[i])
max=-1e10
min=1e10
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
        i1=i
    if a[i]<min:
        min=a[i]
        i2=i
x=a[i1]
a[i1]=a[i2]
a[i2]=x

for i in range(len(a)):
    print(a[i])

