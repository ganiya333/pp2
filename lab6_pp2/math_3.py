import math
num_of_sides=float(input())
length=float(input())
area=(num_of_sides*pow(length,2))/(4*math.tan(math.pi/num_of_sides))
print(area)