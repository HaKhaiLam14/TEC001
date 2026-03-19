def get_season():
    month = int(input("Enter month (1-12): "))
    
    seasons = ("winter", "spring", "summer", "autumn")
    
    if month == 12 or month == 1 or month == 2:
        print(seasons[0])
    elif month >= 3 and month <= 5:
        print(seasons[1])
    elif month >= 6 and month <= 8:
        print(seasons[2])
    elif month >= 9 and month <= 11:
        print(seasons[3])
    else:
        print("Invalid month")


get_season()