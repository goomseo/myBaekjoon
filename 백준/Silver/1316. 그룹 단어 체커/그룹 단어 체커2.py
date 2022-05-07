import sys
input = sys.stdin.readline

def findGroupWord(word):
    # string to list
    # 단어가 어떤 알파벳으로 이루어져 있는지 파악(set)
    wordList = list(word)
    charSet = list(set(word))

    # 특정 알파벳이 최초로 나오는 지점의 인덱스와 마지막으로 나오는 지점의 인덱스 구하고 둘의 차를 리스트에 저장
    idxGaps = []
    for char in charSet:
        idx1 = wordList.index(char)
        tmp = wordList[::-1]
        idx2 = len(word) - (tmp.index(char) + 1)
        idxGaps.append(idx2 - idx1)

    # 몇 종류의 알파벳이 조건을 충족하는지 파악
    count = 0
    for idx in range(len(charSet)):
        if (idxGaps[idx] + 1) == wordList.count(charSet[idx]):
            count += 1

    # 모든 종류의 알파벳이 조건을 충족하면 True, 아니면 False
    if count == len(charSet):
        return True
    else:
        return False

def main():
    # 입력받을 단어의 개수 입력
    # 입력받은 개수만큼 단어 입력
    qtyWords = int(input().rstrip())
    words = [input().rstrip() for _ in range(qtyWords)]
    qtyGroupWords = 0

    # 한 단어씩 검사
    for word in words:
        if findGroupWord(word) == True:
            qtyGroupWords += 1
    
    print(qtyGroupWords)

main()
