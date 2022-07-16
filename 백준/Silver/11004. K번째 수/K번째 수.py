import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
nums = sorted(list(map(int, input().rstrip().split())))

print(nums[K - 1])