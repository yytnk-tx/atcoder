l = []

while True:
    x = int(input())
    if(x == 0):
        break
    l.append(x)

for i, lx in enumerate(l):
    print('Case', str(i+1)+':', lx)
