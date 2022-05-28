import sys
input = sys.stdin.readline

price, qty, money = map(int, input().rstrip().split())
price *= qty

if price > money:
    print(price - money)
else:
    print(0)