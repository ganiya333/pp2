import re
with open('row.txt') as file:
    row = file.read()

result = re.findall('ab{2,3}',row)
print (result)