import sys
input = sys.stdin.readline

receipt = int(input())
priceAndQuantity = [tuple(map(int, input().rstrip().split())) for _ in range(int(input()))]

total = 0
for price, quantity in priceAndQuantity:
    total += (price * quantity)

print('Yes' if receipt == total else 'No')