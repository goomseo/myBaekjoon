import sys
input = sys.stdin.readline

opinions = tuple([input().rstrip() for _ in range(int(input()))])
print('Junhee is not cute!' if opinions.count('1') < opinions.count('0') else 'Junhee is cute!')