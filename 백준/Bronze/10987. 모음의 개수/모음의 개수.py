word = input()

vowelCount = 0
for vowel in ('a', 'e', 'i', 'o', 'u'):
    vowelCount += word.count(vowel)

print(vowelCount)