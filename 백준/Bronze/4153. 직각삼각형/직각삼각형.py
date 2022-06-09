import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    nums = list(map(int, input().split()))

    if (nums[0] == 0) and (nums[1] == 0) and (nums[2] == 0):
        break

    for hypotenuse in nums:
        tmp = nums.copy()
        tmp.remove(hypotenuse)
        if hypotenuse ** 2 == tmp[0] ** 2 + tmp[1] ** 2:
            print('right')
            break
        if nums.index(hypotenuse) == 2:
            print('wrong')