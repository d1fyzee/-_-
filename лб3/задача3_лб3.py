n = int(input("Введите число n: "))
max_sum = 0
best_number = 0
for i in range(1, n + 1):
    current_sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            current_sum += j
    if current_sum > max_sum:
        max_sum = current_sum
        best_number = i
print(f"Число с наибольшей суммой делителей: {best_number}")
print(f"Сумма его делителей: {max_sum}")