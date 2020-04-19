import math

a = float(input())
b = float(input())
c = float(input())
discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    roots = [(-b + math.sqrt(discriminant)) / 2 * a, (-b - math.sqrt(
        discriminant)) / 2 * a]
    print(' '.join(map(str, sorted(roots))))
elif discriminant == 0:
    print((-b + math.sqrt(discriminant)) / 2 * a)
