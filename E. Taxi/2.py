distances = map(int, input().split(' '))
prices = map(int, input().split(' '))
price = 0
for distance, price in zip(sorted(distances), sorted(prices, reverse=True)):
    price += distance * price
print(price)
