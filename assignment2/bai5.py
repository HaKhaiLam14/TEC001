import math

def unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2)  
    area_m2 = area / 10000          
    return price / area_m2


def compare_pizzas():
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))
    
    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))
    
    price1 = unit_price(d1, p1)
    price2 = unit_price(d2, p2)
    
    print("Pizza 1 unit price:", round(price1, 2), "USD/m^2")
    print("Pizza 2 unit price:", round(price2, 2), "USD/m^2")
    
    if price1 < price2:
        print("Pizza 1 gives better value.")
    elif price2 < price1:
        print("Pizza 2 gives better value.")
    else:
        print("Both pizzas have the same value.")