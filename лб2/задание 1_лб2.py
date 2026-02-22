import math
a = float(input("Угол: "))
v = float(input("Скорость: "))
h = float(input("Высота цели: "))
L = float(input("Расстояние: "))
g = 9.81
rad = math.radians(a)
t = L / (v * math.cos(rad))
y = v * math.sin(rad) * t - 0.5 * g * t * t
if 0 <= y <= h:
    print("Попал")
else:
    print("Не попал")