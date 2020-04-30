print(sum(map(lambda x: x[0] * x[1], list(
    zip(sorted(map(int, input().strip().split(' ')), reverse=True),
        sorted(map(int, input().strip().split(' '))))))))
