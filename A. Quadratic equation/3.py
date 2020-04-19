def solve(a, b, c):
    d = (b ** 2) - 4 * a * c
    if d < 0:
        return

    x1 = (-b + d ** (1 / 2)) / 2 * a
    if d == 0:
        print(x1)
        return
    x2 = (-b - d ** (1 / 2)) / 2 * a
    if x1 > x2:
        print(x2, x1)
        return
    print(x1, x2)


a, b, c = float(input()), float(input()), float(input())
solve(a, b, c)
