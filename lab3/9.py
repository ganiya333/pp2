a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])

for i in range (len(a)):
    if i%2==1:
       k=a[i]
       a[i]=a[i-1]
       a[i-1]=k
   

    
for i in range(len(a)):
    print(a[i])