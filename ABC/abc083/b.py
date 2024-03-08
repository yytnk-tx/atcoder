N, A, B = map(int, input().split())

count = 0
for n in range(1, N+1):
    a = n // 10000
    b = (n % 10000) // 1000
    c = (n % 1000) // 100
    d = (n % 100) // 10
    e = n % 10

    if A <= a+b+c+d+e <= B:
        count += n

print(count)
