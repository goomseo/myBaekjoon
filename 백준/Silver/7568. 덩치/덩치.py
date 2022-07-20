import sys
input = sys.stdin.readline

def scaleRank(w_h_list):
    rankings = [1 for _ in range(len(w_h_list))]

    idx = 0
    for w_h in w_h_list:
        for cmp in w_h_list:
            if (w_h[0] < cmp[0]) and (w_h[1] < cmp[1]):
                rankings[idx] += 1

        idx += 1

    for idx in range(len(rankings)):
        rankings[idx] = str(rankings[idx])
        
    return ' '.join(rankings)

def main():
    N = int(input())
    w_h_list = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print(scaleRank(w_h_list))

main()