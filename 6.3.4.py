from math import sin, cos, tan, radians

x = float(input())

rad = radians(x)
res = sin(rad) + cos(rad) + tan(rad) ** 2

print(res)