import sys
input = sys.stdin.readline

input()

num_list = sorted(list(map(int, input().rstrip().split())))
print(num_list[0] * num_list[-1])