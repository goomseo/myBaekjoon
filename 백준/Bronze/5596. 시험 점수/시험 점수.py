scores = [map(int, input().split()) for _ in range(2)]
print(max(sum(scores[0]), sum(scores[1])))