import random

code1 = ""
for i in range(3):
    code1 += str(random.randint(0, 9))

code2 = ""
for i in range(4):
    code2 += str(random.randint(1, 6))

print("3-digit code:", code1)
print("4-digit code:", code2)