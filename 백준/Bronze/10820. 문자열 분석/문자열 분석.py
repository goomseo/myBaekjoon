while True:
    try:    
        string = input()
        lower, upper, num, space = 0, 0, 0, 0

        for char in string:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char == ' ':
                space += 1
            else:
                num += 1

        print(lower, upper, num, space)
    
    except:
        break