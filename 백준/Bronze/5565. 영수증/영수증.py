import sys

def input():
    return sys.stdin.readline().rstrip()

totalPrice = int(input())
prices = sum([int(input()) for _ in range(9)])

print(totalPrice - prices)