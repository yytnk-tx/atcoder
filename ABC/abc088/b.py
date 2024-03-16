N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ap = 0
bp = 0
for i in range(N):
    if i % 2 == 0:
        ap += a[i]
    else:
        bp += a[i]

print(ap - bp)
