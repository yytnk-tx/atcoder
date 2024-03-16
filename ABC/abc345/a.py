import re

S = input()

if re.search(r'^<=+>$', S):
    print('Yes')
else:
    print('No')
