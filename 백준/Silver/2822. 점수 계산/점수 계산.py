import sys
input = sys.stdin.readline

scores = dict(zip([int(input()) for _ in range(8)], [str(num) for num in range(1, 9)]))
totalScore = sorted(list(scores.keys()))[-5:]

print(sum(totalScore))
print(' '.join(sorted([scores[score] for score in totalScore])))