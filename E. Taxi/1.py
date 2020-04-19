kms = input().split(' ')
prices = input().split(' ')

for i in range(len(kms)):
    kms[i] = int(kms[i])
    prices[i] = int(prices[i])

kms = sorted(kms)
prices = sorted(prices)
prices = prices[::-1]

price = 0
for i in range(len(kms)):
    price += kms[i] * prices[i]
print(price)
