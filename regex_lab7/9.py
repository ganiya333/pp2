import re
with open('row.txt') as file:
    row = file.read()

result = re.sub(r'([a-z])([A-Z])', r'\1 \2', row)
print (result)