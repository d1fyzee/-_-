x = int(input("Введите число: "))
q = x
n = len(str(x))
sum_armstrong = 0
while q > 0:
    w = q % 10
    sum_armstrong += w ** n
    q //= 10
if x == sum_armstrong:
    print(f"Число {x} — число Армстронга")
else:
    print(f"Число {x} — не число Армстронга.")