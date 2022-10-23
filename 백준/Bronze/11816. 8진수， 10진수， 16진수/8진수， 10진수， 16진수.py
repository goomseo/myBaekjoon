import sys
input = sys.stdin.readline

num = input().rstrip()

if num[:2] == '0x':
    num = int(num, base = 16)
    print(num)
elif num[0] == '0':
    num = int(num, base = 8)
    print(num)
else:
    print(int(num))