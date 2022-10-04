import sys
input = sys.stdin.readline

num_list = sorted([int(input()) for _ in range(int(input()))])

[print(num) for num in num_list]