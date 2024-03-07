import math

while True:
    n = int(input())

    if n == 0:
        break

    s = list(map(int, input().split()))
    m = sum(s) / n

    sigma = 0
    for i in range(n):
        sigma += (s[i] - m) ** 2
    
    v = sigma / n
    sd = math.sqrt(v)

    print('{:.8f}'.format(sd))
