import sys
input = sys.stdin.readline

def findGW(word):
    wordList = list(word)
    curWord = ''
    wordSet = set()
    for w in wordList:
        if w in wordSet:
            if curWord == w :
                continue
            # elif w in wordSet:#새로운 문자인데 등록된 경우
            else:
                return False
        #         wordSet.add(w)
        #         curWord = w
        else :
            wordSet.add(w)
            curWord = w

    return True

def main():
    # 입력받을 단어의 개수 입력
    # 입력받은 개수만큼 단어 입력
    qtyWords = int(input().rstrip())
    words = [input().rstrip() for _ in range(qtyWords)]
    qtyGroupWords = 0

    # 한 단어씩 검사
    for word in words:
        # if findGroupWord(word) == True:
        if findGW(word) == True:
            qtyGroupWords += 1
    
    print(qtyGroupWords)

main()