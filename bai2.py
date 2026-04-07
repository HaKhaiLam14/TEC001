def find_keyword_lines(filename, keyword):
    lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):  
                if keyword in line:
                    lines.append(i)
        return lines
    except:
        return "Cannot open file"


file = input("Enter file name: ")
key = input("Enter keyword: ")

result = find_keyword_lines(file, key)
print("Keyword found at lines:", result)