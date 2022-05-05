scores = [int(input()) for _ in range(5)]

for i in range(len(scores)):
    if scores[i] < 40:
        scores[i] = 40

print(int(sum(scores) / 5))