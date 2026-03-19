def hemoglobin_check():
    gender = input("Enter biological sex (male/female): ").lower()
    hb = float(input("Enter hemoglobin value (g/l): "))
    
    if gender == "female":
        if hb < 117:
            print("Hemoglobin is low.")
        elif hb <= 155:
            print("Hemoglobin is normal.")
        else:
            print("Hemoglobin is high.")
    
    elif gender == "male":
        if hb < 134:
            print("Hemoglobin is low.")
        elif hb <= 167:
            print("Hemoglobin is normal.")
        else:
            print("Hemoglobin is high.")
    
    else:
        print("Invalid input.")