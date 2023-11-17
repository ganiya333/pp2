s=str(input())
print(s)
s2=''.join(reversed(s))
if s==s2:
    print("YES")
else:
    print ("NO")
    