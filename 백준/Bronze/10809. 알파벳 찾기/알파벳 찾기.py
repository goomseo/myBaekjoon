import sys
from string import ascii_lowercase
input = sys.stdin.readline
alphabetList = list(ascii_lowercase)

word = input()

for i in alphabetList:
    if i in word:
        print(word.index(i), end = ' ')
    else:
        print(-1, end = ' ')