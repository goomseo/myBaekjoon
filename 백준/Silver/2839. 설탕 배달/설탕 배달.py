import sys
input = sys.stdin.readline

sugar = int(input())

bags = 0
while sugar:
    if not(sugar % 5):
        bags += (sugar // 5)
        print(bags)
        break
    
    if sugar >= 3:
        sugar -= 3
        bags += 1

        if not sugar:
            print(bags)
    else:
        print(-1)
        break