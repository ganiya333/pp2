n=int(input())
m=int(input())
x=int(input())
y=int(input())
if n>m:
    res1=m-x
    res2=n-y
    print(min(x,y,res1,res2))
else:
    res1=n-x
    res2=m-y
    print(min(x,y,res1,res2))