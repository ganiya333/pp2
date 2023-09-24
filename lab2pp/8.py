x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
sum1=int(x1+y1)
sum2=int(x2+y2)
if sum1<=(sum2+2) and sum1>=(sum2-2):
    print("YES")
else:
    print("NO")
