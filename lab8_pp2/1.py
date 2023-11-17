import math
def multiply_numbers(x):
    answer=math.prod(x)
    return answer
    
a=[int(s) for s in input().split()]
ans=multiply_numbers(a)
print (ans)


