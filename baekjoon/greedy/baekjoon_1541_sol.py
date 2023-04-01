import sys
element, result = sys.stdin.readline().rstrip().split('-'), 0

for i in element[0].split('+'):
    result += int(i)

for i in element[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)