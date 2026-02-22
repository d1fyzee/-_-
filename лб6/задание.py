def parse_and_calculate(file_path):
    # Словарик для хранения ключей и значений из заголовка
    header_data = {}
    # Двумерный массив (список списков) для хранения таблицы измерений
    measurements = []

    # Открываем файл для чтения
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Убираем лишние пробелы и символы переноса строки по краям
            line = line.strip()

            # Пропускаем пустые строки
            if not line:
                continue

            # 1. ОБРАБОТКА ЗАГОЛОВКА (Ключ : Значение)
            if line.startswith('%'):
                # Ищем первое двоеточие. В строке может быть время (00:00:00),
                # поэтому делим строку только по ПЕРВОМУ двоеточию (maxsplit=1)
                if ':' in line:
                    parts = line.split(':', 1)

                    # Очищаем ключ (убираем % и пробелы)
                    key = parts[0].replace('%', '').strip()
                    # Очищаем значение
                    value = parts[1].strip()

                    # Проверяем, есть ли уже такой ключ
                    if key in header_data:
                        # Если там уже список, просто добавляем новое значение
                        if isinstance(header_data[key], list):
                            header_data[key].append(value)
                        # Если там было одно значение, превращаем его в список из двух элементов
                        else:
                            header_data[key] = [header_data[key], value]
                    else:
                        # Если ключа не было, просто записываем значение
                        header_data[key] = value

            # 2. ОБРАБОТКА ТАБЛИЦЫ ИЗМЕРЕНИЙ
            else:
                # Если строка не начинается с %, значит это данные.
                # Функция split() без параметров сама разобьет строку по всем пробелам
                columns = line.split()
                # Добавляем строку в наш двумерный массив
                measurements.append(columns)

    # 3. РАСЧЕТ СРЕДНИХ ЗНАЧЕНИЙ X, Y, Z
    # Переменные для суммы
    sum_x = 0.0
    sum_y = 0.0
    sum_z = 0.0

    count = len(measurements)  # Общее количество строк с измерениями

    # Проходимся по каждой строке в двумерном массиве
    for row in measurements:
        # Индексы: 0-Дата, 1-Время, 2-X, 3-Y, 4-Z
        # Переводим текст в дробные числа (float) и прибавляем к суммам
        sum_x += float(row[2])
        sum_y += float(row[3])
        sum_z += float(row[4])

    # Считаем среднее
    avg_x = sum_x / count
    avg_y = sum_y / count
    avg_z = sum_z / count

    return header_data, avg_x, avg_y, avg_z


# --- ЗАПУСК ПРОГРАММЫ ---
# Предполагается, что файл лежит в той же папке и называется '08.pos'
parsed_header, average_x, average_y, average_z = parse_and_calculate('08.pos')

# Выводим результаты
print("--- Извлеченные ключи и значения (пример) ---")
print(f"Программа: {parsed_header.get('program')}")
print(f"Входные файлы (список):")
for file_name in parsed_header.get('inp file', []):
    print(f" - {file_name}")

print("\n--- Средние координаты ---")
print(f"Среднее X: {average_x}")
print(f"Среднее Y: {average_y}")
print(f"Среднее Z: {average_z}")