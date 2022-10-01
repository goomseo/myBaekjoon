import sys
input = sys.stdin.readline

A = int(input())
operator = input().rstrip()
B = int(input())

print(A + B if operator == '+' else A * B)