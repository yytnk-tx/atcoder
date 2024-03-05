r, c = map(int, input().split())
a = []

for _ in range(r):
    a.append(list(map(int, input().split())))

colnum = [0] * c
for i in range(r):
    rownum = 0
    for j in range(c):
        print(a[i][j], end=' ')
        rownum += a[i][j]
        colnum[j] += a[i][j]
    print(rownum, end='')
    print()

total = 0
for j in range(c):
    total += colnum[j]
    print(colnum[j], end=' ')

print(total)
