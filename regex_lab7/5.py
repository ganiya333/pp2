import re
with open('row.txt') as file:
    row = file.read()

result = re.search('a.*?b$',row)
print (result)