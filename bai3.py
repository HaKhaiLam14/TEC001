def average_score(filename):
    total = 0
    count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    name, score = line.strip().split(',')
                    total += float(score)
                    count += 1
        return total / count if count != 0 else 0
    except:
        return "Cannot open or read file"


file = input("Enter file name: ")
result = average_score(file)
print("Average score:", result)