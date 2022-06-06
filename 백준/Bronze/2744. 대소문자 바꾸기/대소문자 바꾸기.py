import sys
input = sys.stdin.readline

word = input()

newWord = ''
for char in word:
    if char.isupper():
        newWord += char.lower()
    else:
        newWord += char.upper() 

print(newWord)