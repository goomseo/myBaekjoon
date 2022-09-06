import sys
input = sys.stdin.readline

censorship = 'CAMBRIDGE'

word = input().rstrip()

for char in word:
    if char in censorship:
        word = word.replace(char, '')

print(word)