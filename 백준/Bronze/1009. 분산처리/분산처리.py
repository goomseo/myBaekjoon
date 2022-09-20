import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    
    answer = ((a % 10) ** (b % 4 + 4)) % 10
    print(10 if not answer else answer)