def count_lines(filename):
    count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():  
                    count += 1
        return count
    except:
        return "Cannot open file"

# main program
file = input("Enter file name: ")
print("Number of non-empty lines:", count_lines(file))