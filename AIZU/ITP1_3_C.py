l = []

while True:
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        break

    if x > y:
        x, y = y, x
    l.append([x, y])

for li in l:
    print(li[0], li[1])
