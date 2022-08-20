import sys
input = sys.stdin.readline

fileNames = [input().rstrip() for _ in range(int(input()))]

pattern = list(fileNames[0])
for fileName in fileNames[1:]:
    for idx in range(len(fileName)):
        if pattern[idx] != fileName[idx]:
            pattern[idx] = '?'

print(''.join(pattern))