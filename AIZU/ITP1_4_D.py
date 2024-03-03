n = int(input())

min = 1000001
max = -1000001
sum = 0

input = list(map(int, input().split()))

for a in input:
    if min > a:
        min = a
    if max < a:
        max = a
    sum += a

print(min, max, sum)
