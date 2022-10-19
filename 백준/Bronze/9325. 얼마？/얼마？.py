import sys
input = sys.stdin.readline

for _ in range(int(input())):
    carPrice = int(input())
    for _ in range(int(input())):
        q, p = map(int, input().rstrip().split())
        carPrice += q * p
    
    print(carPrice)