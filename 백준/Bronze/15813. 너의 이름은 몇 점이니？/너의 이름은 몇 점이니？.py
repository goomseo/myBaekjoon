import sys
input = sys.stdin.readline

input()
print(sum([ord(char) - 64 for char in list(input().rstrip())]))