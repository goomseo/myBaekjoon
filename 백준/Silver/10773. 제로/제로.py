import sys
input = sys.stdin.readline

nums = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        del nums[-1]
    else:
        nums.append(num)

print(sum(nums))