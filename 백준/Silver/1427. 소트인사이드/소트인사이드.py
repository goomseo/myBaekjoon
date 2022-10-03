import sys
input = sys.stdin.readline

n = input().rstrip()
num_list = sorted([int(char) for char in n], reverse = True)

print(''.join(map(str, num_list)))