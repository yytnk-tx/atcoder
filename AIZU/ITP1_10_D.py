import math

def minkowski(n, x, y, p):
    sigma = 0
    for i in range(n):
        sigma += abs(x[i] - y[i]) ** p

    return sigma ** (p ** -1)

def minkowski_inf(n, x, y):
    max_value = -2001
    for i in range(n):
        if max_value < abs(x[i] - y[i]):
            max_value = abs(x[i] - y[i])

    return max_value

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print('{:.6f}'.format(minkowski(n, x, y, 1)))
print('{:.6f}'.format(minkowski(n, x, y, 2)))
print('{:.6f}'.format(minkowski(n, x, y, 3)))
print('{:.6f}'.format(minkowski_inf(n, x, y)))
