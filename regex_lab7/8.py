import re
with open('row.txt') as file:
    row = file.read()

result = re.findall('[A-Z][^A-Z]*', row)
print (result)