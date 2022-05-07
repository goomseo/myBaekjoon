import sys
input = sys.stdin.readline

burgers = [int(input().rstrip()) for _ in range(3)]
drinks = [int(input().rstrip()) for _ in range(2)]

print(min(burgers) + min(drinks) - 50)