import sys
input = sys.stdin.readline

rpt = int(input())

for _ in range(rpt):
    string = input().rstrip()
    print(f'{string[0]}{string[-1]}')