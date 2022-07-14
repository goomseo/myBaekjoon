import sys
input = sys.stdin.readline

classNum = 0

def getScores():
    global classNum
    classNum += 1
    
    scores = sorted(list(map(int, input().rstrip().split()))[1:])
    
    largestGap = [0]
    for idx in range(len(scores) - 1):
        gap = scores[idx + 1] - scores[idx]
        if gap > largestGap[0]:
            largestGap = [gap]

    print(f'Class {classNum}\nMax {max(scores)}, Min {min(scores)}, Largest gap {largestGap[0]}')

    largestGap.clear()

def main():
    K = int(input())

    for _ in range(K):
        getScores()

main()