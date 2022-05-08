import math
import sys
input = sys.stdin.readline

endNum = int(input().rstrip())
print(1 + math.ceil((-3 + math.sqrt((12 * endNum) - 3)) / 6))