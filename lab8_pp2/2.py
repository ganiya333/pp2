def count_fun(string):
    
    num_of_upper = sum(1 for char in string if char.isupper())
    num_of_lower = sum(1 for char in string if char.islower())
    return  num_of_upper, num_of_lower

s=str(input())
upper, lower = count_fun(s)
print(f"Num of upper: {upper}")
print(f"Num of lower: {lower}")