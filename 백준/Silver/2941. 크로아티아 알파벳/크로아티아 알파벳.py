import sys
input = sys.stdin.readline

word = input().rstrip()

croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

total = len(word)
for c in croatian:
    if c in word:
        total -= word.count(c)

print(total)