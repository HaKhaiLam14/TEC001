while(True):
    i = input("Enter your inches: ")
    check = True
    try:
        i = int(i)
    except:
        print("Invalid value!")
        check = False
    if(check):
        if(i < 0):
            print("bye bye!")
            break
        print(f"{i} inches = {i*2.54} cm")
    
    