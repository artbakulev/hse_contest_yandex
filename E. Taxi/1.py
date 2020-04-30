kms = map(int, input().strip().split(' '))
prices = map(int, input().strip().split(' '))

kms = sorted(kms)
prices = sorted(prices, reverse=True)

price = 0
for i in range(len(kms)):
    price += kms[i] * prices[i]
print(price)
