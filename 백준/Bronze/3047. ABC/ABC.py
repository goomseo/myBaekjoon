import sys
input = sys.stdin.readline

nums = map(int, input().rstrip().split())
abc = input().rstrip()
abc_nums = dict(zip(sorted(abc), sorted(nums)))

for char in abc:
    print(abc_nums[char], end = ' ')