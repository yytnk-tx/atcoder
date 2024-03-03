l = []

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    l.append([H, W])

for li in l:
    for _ in range(li[0]):
        for _ in range(li[1]):
            print('#', end='')
        print()
    print()
