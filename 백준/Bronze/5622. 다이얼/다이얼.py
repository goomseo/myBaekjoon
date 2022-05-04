def alphaToDialnum(char):
    alphabets = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
    for l in alphabets:
        if char in l:
            return alphabets.index(l) + 3


word = input()

total = 0
for char in word:
        total += alphaToDialnum(char)

print(total)
