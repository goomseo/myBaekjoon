import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    nums = list(map(int, input().split()))

    if not sum(nums):
        break

    hypotenuse = max(nums)
    nums.remove(hypotenuse)

    print('right' if (hypotenuse ** 2) == ((nums[0] ** 2) + (nums[1] ** 2)) else 'wrong')