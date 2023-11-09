import re
with open('row.txt') as file:
    row = file.read()

result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', row)
print (result)