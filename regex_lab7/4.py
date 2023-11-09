import re
with open('row.txt') as file:
    row = file.read()

result = re.findall(r'\b[A-Z][a-z]+\b',row)
print (result)