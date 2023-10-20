def filter_prime(x):
    if x<=1:
        return False
    if x==2:
        return True
    flag=True
    for i in range(2,x):
        if x%i==0:
            return False
            break
    return flag
    
    
a=input().split()
for i in range(len(a)):
    a[i]=int(a[i])

for i in range (len(a)):
    if filter_prime(a[i])==True:
        print(a[i], end=" ")