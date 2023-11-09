import re
with open('row.txt') as file:
    row = file.read()

result = re.findall(r'\b[a-z]+_[a-z]+\b',row)
print (result)