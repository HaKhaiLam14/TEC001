def check_zander():
    length = float(input("Enter the length of the zander (cm): "))
    
    if length < 42:
        print("Release the fish back into the lake!")
        print("It is", 42 - length, "cm below the size limit.")
    else:
        print("The fish meets the size limit.")