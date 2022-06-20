import sys
input = sys.stdin.readline

coordinates = sorted([tuple(map(int, input().rstrip().split())) for _ in range(int(input()))])

[print(f'{coordinate[0]} {coordinate[1]}') for coordinate in coordinates]