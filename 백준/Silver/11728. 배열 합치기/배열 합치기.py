import sys
input = sys.stdin.readline

input()
arr1 = list(map(int, input().rstrip().split()))
arr2 = list(map(int, input().rstrip().split()))

[print(num, end = ' ') for num in sorted(arr1 + arr2)]