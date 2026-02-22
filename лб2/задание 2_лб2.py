print("Введите границы первого отрезка:")
a = float(input())
b = float(input())
print("Введите границы второго отрезка:")
c = float(input())
d = float(input())
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

if b < c or d < a:
    print("Не пересекаются")
else:
    print("Пересекаются")