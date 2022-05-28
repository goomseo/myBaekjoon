import sys
input = sys.stdin.readline

price, qty, money = map(int, input().rstrip().split())
price *= qty

print(price - money if price - money > 0 else 0)