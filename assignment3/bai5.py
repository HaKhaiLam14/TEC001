s = input()

def mid_character(s:str):
    if(len(s) % 2 == 0):
        print(s[len(s) // 2 - 1])
        print(s[len(s) // 2])
    else:
        print(s[len(s) // 2])

mid_character(s)