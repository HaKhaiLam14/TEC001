s = input()

def short_cpital(s:str):
    s = s.upper()
    s2 = s.split()
    for i in s2:
        print(i[0], end='')

short_cpital(s)
    