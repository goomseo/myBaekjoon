import sys
input = sys.stdin.readline

registances  = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 
                'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

colors = [input().rstrip() for _ in range(3)]

print(int(str(registances[colors[0]]) + str(registances[colors[1]])) * (10 ** registances[colors[2]]))