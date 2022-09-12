import sys
input = sys.stdin.readline

bins = input().rstrip().split()
bins[0] = int(bins[0], 2)
bins[1] = int(bins[1], 2)

print(bin(sum(bins))[2:])