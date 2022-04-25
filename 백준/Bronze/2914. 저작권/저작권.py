import sys
input = sys.stdin.readline

qtySong, avg = map(int, input().split())

print((qtySong * (avg-1)) + 1)