import sys
input = sys.stdin.readline

def findGroupWord(word):
    wordList = list(word)
    charSet = list(set(word))

    idxGaps = []
    for char in charSet:
        idx1 = wordList.index(char)
        reversedWordList = wordList[::-1]
        idx2 = len(word) - (reversedWordList.index(char) + 1)
        idxGaps.append(idx2 - idx1 + 1)

    count = 0
    for i in range(len(charSet)):
        if idxGaps[i] == wordList.count(charSet[i]):
            count += 1

    if count == len(charSet):
        return True
    else:
        return False

def main():
    qtyWords = int(input().rstrip())
    words = [input().rstrip() for _ in range(qtyWords)]
    qtyGroupWords = 0

    for word in words:
        if findGroupWord(word) == True:
            qtyGroupWords += 1
    
    print(qtyGroupWords)

main()