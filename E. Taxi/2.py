distances = map(int, input().split(' '))
prices = map(int, input().split(' '))
total_price = 0
for distance, price in zip(sorted(distances), sorted(prices, reverse=True)):
    total_price += distance * price
print(total_price)
