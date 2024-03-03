l = []

while True:
    a, op, b = input().split()
    if op == '?':
        break
    else:
        l.append({'a':a, 'op':op, 'b':b})

for li in l:
    if li['op'] == '+':
        print(int(li['a']) + int(li['b']))
    elif li['op'] == '-':
        print(int(li['a']) - int(li['b']))
    elif li['op'] == '*':
        print(int(li['a']) * int(li['b']))
    elif li['op'] == '/':
        print(int(li['a']) // int(li['b']))
