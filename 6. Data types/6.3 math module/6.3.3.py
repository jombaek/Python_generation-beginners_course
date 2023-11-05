from math import sqrt, pow

a = float(input())
b = float(input())

arithmetic_mean = (a + b) / 2
geometric_mean = sqrt(a * b)
harmonic_mean = 2 * a * b / (a + b)
quadratic_mean = sqrt((pow(a, 2) + pow(b, 2)) / 2)

print(arithmetic_mean)
print(geometric_mean)
print(harmonic_mean)
print(quadratic_mean)