import re
with open('pr.txt', 'r') as file:
    content = file.read()
pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}')
res = pattern.findall('r')
print(res)
