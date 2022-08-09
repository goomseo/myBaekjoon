import sys
input = sys.stdin.readline

num1, num2 = input().split()

total = 0
for i in num1:
    for j in num2:
        total += int(i) * int(j)

print(total)