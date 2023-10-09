students = [{input() for j in range(int(input()))} for i in range(int(input()))]
x1, x2 = set.intersection(*students), set.union(*students)
print(len(x1), *sorted(x1), sep='\n')
print(len(x2), *sorted(x2), sep='\n')