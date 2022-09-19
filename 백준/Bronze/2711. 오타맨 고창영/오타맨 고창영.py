import sys
input = sys.stdin.readline

for _ in range(int(input())):
    idx, word = input().rstrip().split()
    word = word[:(int(idx)-1)] + word[int(idx):]
    print(word)