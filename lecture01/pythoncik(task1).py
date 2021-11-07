import math
a = int(input())
b = int(input())
ugolGrad = int(input())
if (ugolGrad > 1 and ugolGrad < 360):
    ugolRad = math.radians(ugolGrad)
    c = math.sqrt(a**2 + b**2 - 2*math.cos(ugolRad)*a*b)
print(c)
