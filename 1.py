import re
with open('row.txt') as file:
    row = file.read()

result = re.findall('a.*b',row)
print (result)