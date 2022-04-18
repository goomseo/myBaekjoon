import sys
input = sys.stdin.readline

qty = int(input())
nums = list(input())

total = 0
for i in range(qty):
    nums[i] = int(nums[i])
    total += nums[i]

print(total)