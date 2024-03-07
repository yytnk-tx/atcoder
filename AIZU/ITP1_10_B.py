import math
a, b, C = map(int, input().split())

h = b * math.sin(math.radians(C))
S = float((a * h) / 2)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))
L = a + b + c

print('{:.8f}'.format(S))
print('{:.8f}'.format(L))
print('{:.8f}'.format(h))
