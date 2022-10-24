word = input().rstrip()

print('true' if word == word[::-1] else 'false')