n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append([])
    a[i] = list(map(int, input().split()))

for i in range(m):
    b.append(int(input()))

c = []

for i in range(n):
    c.append(0)
    for j in range(m):
        c[i] += a[i][j] * b[j]
    print(c[i])
