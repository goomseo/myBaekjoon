import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]

print(sum(nums) // len(nums))
print(max(nums, key = lambda i: nums.count(i)))