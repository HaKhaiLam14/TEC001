numbers = []

while True:
    num = input("Enter a number (empty to quit): ")
    
    if num == "":
        break
    
    numbers.append(float(num))

numbers.sort(reverse=True)

top5 = numbers[:5]

print("Top 5 numbers:", top5)