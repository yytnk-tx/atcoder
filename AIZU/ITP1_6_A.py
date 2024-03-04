n = int(input())
l = list(map(int, input().split()))

print(l.pop(-1), end='')
for _ in range(n-1):
    print(' ' + str(l.pop(-1)),end='')
print()
