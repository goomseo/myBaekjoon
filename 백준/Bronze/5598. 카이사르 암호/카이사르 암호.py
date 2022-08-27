import sys
input = sys.stdin.readline

def convert(char):
    if char == 'A':
        return 'X'
    elif char == 'B':
        return 'Y'
    elif char == 'C':
        return 'Z'
    else:
        return chr(ord(char) - 3)

[print(convert(char), end = '') for char in input().rstrip()]