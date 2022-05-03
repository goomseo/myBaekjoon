import sys
input = sys.stdin.readline

summerDay, growUpDay, qtyFruit, price = map(int, input().split())
print(((summerDay - 1) // growUpDay) * qtyFruit * price)