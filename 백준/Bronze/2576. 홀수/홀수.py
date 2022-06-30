import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(7)]
for num in nums.copy():
    if num % 2 == 0:
        nums.remove(num)

print(f'{sum(nums)}\n{min(nums)}' if len(nums) != 0 else -1)