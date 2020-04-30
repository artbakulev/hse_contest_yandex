distances, prices = list(map(int, input().strip().split(' '))), \
                    list(map(int, input().strip().split(' ')))
distances.sort()
prices.sort()
prices.reverse()
price = 0
for i in range(len(prices)):
    price += int(distances[i]) * int(prices[i])
print(price)
