import random
x = 1
while x < 4:
    x += 1
    int_num1 = random.randint(1, 6)
    int_num2 = random.randint(1, 6)
    int_num3 = random.randint(1, 6)
    a = str(int_num1 + int_num2 + int_num3)
    s = int(a)
print(s**2)


