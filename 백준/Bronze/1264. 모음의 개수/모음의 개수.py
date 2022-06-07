import sys
input = sys.stdin.readline

vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
while True:
    tc = input().rstrip()

    if tc == '#':
        break
    
    qtyVowel = 0
    for char in tc:
        if char in vowels:
            qtyVowel += 1
    
    print(qtyVowel)