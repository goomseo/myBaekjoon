from string import ascii_lowercase

word = input()

for char in ascii_lowercase:
    print(word.count(char), end = ' ')