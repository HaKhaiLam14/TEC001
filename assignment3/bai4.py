
username = "python"
password = "rules"

count = 0
while True: 
    a = input("Enter your username: ")
    b = input("Enter your password: ")
    count = count + 1
    if(a == username and b == password):
        print("Welcome")
        break
    elif(count == 5):
        print(f"wrong {count} times, Access denied")
        break
    else:
        print(f"wrong {count} times")
    