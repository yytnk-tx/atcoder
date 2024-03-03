import math

r = float(input())

area = r * r * math.pi
rad = 2 * r * math.pi

print('{:.6f} {:.6f}'.format(area, rad))
