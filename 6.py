import re
with open('row.txt') as file:
    row = file.read()

result = re.sub(r'[ ,.]', ':', row)
print (result)