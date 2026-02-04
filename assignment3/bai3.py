from math import inf

min_n = inf
max_n = -inf

while(True):
    n = input("Enter your number: ")
    try:
        n = int(n)
    except:
        print("bye bye!")
        break
    if n < min_n:
        min_n = n
    if n > max_n:
        max_n = n

print("Min:", min_n)
print("Max:", max_n)