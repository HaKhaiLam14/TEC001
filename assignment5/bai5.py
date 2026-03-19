import random

def approximate_pi():
    n = int(input("Enter number of random points: "))
    
    inside_circle = 0
    
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x**2 + y**2 < 1:
            inside_circle += 1
    
    pi = 4 * inside_circle / n
    
    print("Approximation of pi:", pi)


approximate_pi()