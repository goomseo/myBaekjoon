import sys

def input():
    return sys.stdin.readline().rstrip()

score = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0}

grade = input()

for alphabet in score.keys():
    if grade == 'F':
        print(0.0)
        break

    if grade[0] == alphabet:
        if grade[1] == '+':
            print(score[grade[0]] + 0.3)
        elif grade[1] == '-':
            print(score[grade[0]] - 0.3)
        else:
            print(score[grade[0]])