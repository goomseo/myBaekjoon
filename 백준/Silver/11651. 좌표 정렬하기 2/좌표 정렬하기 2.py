import sys
input = sys.stdin.readline

coordinates = sorted([list(reversed(list(map(int, input().rstrip().split())))) for _ in range(int(input()))])

[print(f'{coordinate[1]} {coordinate[0]}') for coordinate in coordinates]