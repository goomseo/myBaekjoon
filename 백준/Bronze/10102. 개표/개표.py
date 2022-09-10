import sys
input = sys.stdin.readline

input()
votes = list(input().rstrip())

if votes.count('A') > votes.count('B'):
    print('A')
elif votes.count('A') < votes.count('B'):
    print('B')
else:
    print('Tie')