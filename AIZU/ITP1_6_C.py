corp = {}

n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    key = str(b) + str(f) + str(r)

    if key in corp:
        corp[key] += v
    else:
        corp[key] = v

for b in range(1, 5):
    for f in range(1, 4):
        for r in range(1, 11):
            key = str(b) + str(f) + str(r)
            if key in corp:
                print(' ' + str(corp[key]), end='')
            else:
                print(' 0', end='')
        print()
    if b != 4:
        print('####################')
