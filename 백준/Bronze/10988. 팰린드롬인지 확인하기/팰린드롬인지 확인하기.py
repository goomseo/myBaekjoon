import sys

def input():
    return sys.stdin.readline().rstrip()

word = input()

print(1 if word == word[::-1] else 0)