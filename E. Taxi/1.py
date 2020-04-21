kms = map(int, input().split(' '))
prices = map(int, input().split(' '))

kms = sorted(kms)
prices = sorted(prices, reverse=True)

price = 0
for i in range(len(kms)):
    price += kms[i] * prices[i]
print(price)
