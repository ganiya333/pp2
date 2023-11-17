import math
import time
def sq_root(a,b):
     time.sleep(b/1000) 
     return math.sqrt(a)
a=float(input())
b=int(input())
ans=sq_root(a,b)
print(f"Square root of {a} after {b} milliseconds is {ans}")