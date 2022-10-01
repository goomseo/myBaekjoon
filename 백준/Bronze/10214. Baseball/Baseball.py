import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score_dict = {'Yonsei': 0, 'Korea': 0}
    for _ in range(9):
        Y, K = map(int, input().rstrip().split())
        score_dict['Yonsei'] += Y
        score_dict['Korea'] += K
    
    if score_dict['Yonsei'] > score_dict['Korea']:
        print('Yonsei')
    elif score_dict['Yonsei'] < score_dict['Korea']:
        print('Korea')
    else:
        print('Draw')