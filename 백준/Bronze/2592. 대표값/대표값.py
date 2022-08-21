import statistics
import sys
input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]

print(statistics.mean(nums))
print(statistics.mode(nums))