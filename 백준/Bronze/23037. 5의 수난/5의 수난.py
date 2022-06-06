import sys
input = sys.stdin.readline

num = input().rstrip()

total = 0
for char in num:
    total += int(char) ** 5

print(total)