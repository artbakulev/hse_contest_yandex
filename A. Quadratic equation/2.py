a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d >= 0:
    x1 = (-b + d ** (1 / 2)) / 2 * a
    if d > 0:
        x2 = (-b - d ** (1 / 2)) / 2 * a
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
    else:
        print(x1)
