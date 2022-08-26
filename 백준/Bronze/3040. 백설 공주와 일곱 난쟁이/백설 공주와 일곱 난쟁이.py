import sys
from itertools import combinations
input = sys.stdin.readline

nums = [int(input()) for _ in range(9)]

for combination in tuple(combinations(nums, 2)):
    if sum(nums) - sum(combination) == 100:
        nums.remove(combination[0])
        nums.remove(combination[1])

        [print(num) for num in nums]
        break