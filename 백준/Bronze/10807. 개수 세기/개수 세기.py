import sys
input = sys.stdin.readline

input()
nums = list(map(int, input().rstrip().split()))
target = int(input().rstrip())

print(nums.count(target))